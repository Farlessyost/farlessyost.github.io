"""Export portfolio views from the saved engineering models, without UI overlays.

Run with FreeCAD's Python runtime; requires VTK. Source documents are read only.
"""
import argparse
import hashlib
import json
import math
import subprocess

import numpy as np
from PIL import Image
from vtk.util.numpy_support import vtk_to_numpy
from pathlib import Path

import FreeCAD as App
import vtk
import papaw_components as hardware
import xyz_appearance

parser = argparse.ArgumentParser()
parser.add_argument('--papaw-cad', type=Path, required=True)
parser.add_argument('--xyz-cad', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--only', help='Render this output filename, or all papaw/xyz views')
parser.add_argument('--ffmpeg', required=True, type=Path)
parser.add_argument('--review-dir', required=True, type=Path)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
args.review_dir.mkdir(parents=True, exist_ok=True)
provenance = {}


def open_model(path):
    provenance[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return App.openDocument(str(path))


def actor_for(shape, color, opacity=1, offset=None, finish=None):
    vertices, faces = shape.tessellate(.15)
    points = vtk.vtkPoints()
    for p in vertices:
        points.InsertNextPoint(p.x, p.y, p.z)
    triangles = vtk.vtkCellArray()
    for face in faces:
        triangles.InsertNextCell(3)
        for i in face:
            triangles.InsertCellPoint(i)
    mesh = vtk.vtkPolyData()
    mesh.SetPoints(points)
    mesh.SetPolys(triangles)
    if finish == 'wood':
        mesh = xyz_appearance.wood_mesh(vertices, faces)
    normals = vtk.vtkPolyDataNormals()
    normals.SetInputData(mesh)
    normals.SetFeatureAngle(45)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(normals.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    prop = actor.GetProperty()
    prop.SetColor(*color)
    prop.SetOpacity(opacity)
    prop.SetAmbient(.38)
    prop.SetDiffuse(.65)
    prop.SetSpecular(.18)
    prop.SetSpecularPower(35)
    finishes = {
        'metal': (.22, .68, .85, 80),
        'plastic': (.30, .70, .24, 35),
        'rubber': (.32, .75, .06, 20),
        'glass': (.22, .40, .95, 100),
        'wood': (.35, .70, .04, 15),
    }
    if finish in finishes:
        ambient, diffuse, specular, power = finishes[finish]
        prop.SetAmbient(ambient)
        prop.SetDiffuse(diffuse)
        prop.SetSpecular(specular)
        prop.SetSpecularPower(power)
    if finish == 'wood':
        actor.SetTexture(xyz_appearance.wood_texture())
    if offset:
        actor.SetPosition(*offset)
    return actor


def render(name, parts, direction, up=(0, 0, 1)):
    if args.only and args.only != name and not (
            args.only in ('papaw', 'xyz') and name.startswith(args.only + '-')):
        return
    width, height, frames, fps = 960, 640, 120, 12.5
    if name == 'papaw-family-current.png':
        width, height, frames, fps = 720, 480, 96, 10
    renderer = vtk.vtkRenderer()
    # Match the owner's FreeCAD viewport color (#1f1f1f).
    renderer.SetBackground(31 / 255, 31 / 255, 31 / 255)
    renderer.SetUseDepthPeeling(True)
    renderer.SetMaximumNumberOfPeels(100)
    renderer.SetUseFXAA(True)
    corners = []
    for part in parts:
        actor = actor_for(*part)
        renderer.AddActor(actor)
        bounds = actor.GetBounds()
        corners.extend((x, y, z) for x in bounds[:2]
                       for y in bounds[2:4] for z in bounds[4:])
    camera = renderer.GetActiveCamera()
    camera.SetPosition(*direction)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetViewUp(*up)
    camera.ParallelProjectionOn()
    renderer.ResetCamera()
    center = np.asarray(camera.GetFocalPoint())
    points = np.asarray(corners) - center
    # Use one fixed scale that fits the assembly at every rotation angle.
    elevation = math.atan2(direction[2], math.hypot(*direction[:2]))
    scale = 0
    for i in range(frames):
        angle = 2 * math.pi * i / frames
        view = np.array([math.cos(angle) * math.cos(elevation),
                         math.sin(angle) * math.cos(elevation), math.sin(elevation)])
        right = np.cross(view, np.asarray(up, dtype=float))
        right /= np.linalg.norm(right)
        vertical = np.cross(right, view)
        scale = max(scale, np.max(np.abs(points @ vertical)),
                    np.max(np.abs(points @ right)) / (width / height))
    camera.SetParallelScale(float(scale * 1.06))
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(True)
    window.SetAlphaBitPlanes(True)
    window.SetMultiSamples(0)
    window.SetSize(width, height)
    window.AddRenderer(renderer)
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.SetInputBufferTypeToRGB()
    capture.ReadFrontBufferOff()
    gif = args.output / name.replace('.png', '.gif')
    # Jekyll ignores hidden files. Publish each completed file with an atomic
    # rename so its watcher cannot copy an animation while it is being encoded.
    staged_gif = gif.with_name('.' + gif.name)
    staged_poster = args.output / ('.' + name)
    log_path = args.review_dir / (gif.stem + '.log')
    command = [str(args.ffmpeg), '-y', '-loglevel', 'error', '-f', 'rawvideo',
               '-pixel_format', 'rgb24', '-video_size', f'{width}x{height}',
               '-framerate', str(fps), '-i', 'pipe:0', '-filter_complex',
               '[0:v]split[a][b];[a]palettegen=stats_mode=full[p];'
               '[b][p]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle',
               '-loop', '0', str(staged_gif)]
    with log_path.open('wb') as log:
        encoder = subprocess.Popen(command, stdin=subprocess.PIPE, stderr=log)
        try:
            for i in range(frames):
                renderer.ResetCameraClippingRange()
                window.Render()
                capture.Modified()
                capture.Update()
                pixels = vtk_to_numpy(capture.GetOutput().GetPointData().GetScalars())
                pixels = pixels.reshape(height, width, 3)[::-1].copy()
                if i == 0:
                    Image.fromarray(pixels).save(staged_poster)
                if i % (frames // 4) == 0:
                    Image.fromarray(pixels).save(args.review_dir / f'{gif.stem}-{i:03d}.png')
                encoder.stdin.write(pixels.tobytes())
                camera.Azimuth(360 / frames)
                if (i + 1) % 30 == 0:
                    print(f'{gif.name}: {i + 1}/{frames} frames', flush=True)
            encoder.stdin.close()
            if encoder.wait() != 0:
                raise RuntimeError(log_path.read_text())
            staged_gif.replace(gif)
            staged_poster.replace(args.output / name)
        finally:
            if encoder.poll() is None:
                encoder.kill()
                encoder.wait()
            staged_gif.unlink(missing_ok=True)
            staged_poster.unlink(missing_ok=True)
            window.Finalize()
    print(f'Rendered {gif.name}: {gif.stat().st_size:,} bytes', flush=True)


def battery_color(name):
    if 'frame' in name.lower(): return (.09, .52, .52)
    if 'cells' in name.lower(): return (.09, .11, .14)
    if 'leaves' in name.lower(): return (.76, .65, .39)
    if 'Positive' in name: return (.76, .12, .10)
    if 'Joint' in name: return (.60, .64, .68)
    return (.12, .16, .20)


def papaw_scene(module, exploded):
    filenames = {'sensor': 'compact_pir_node.FCStd',
                 'door': 'compact_magnetic_node.FCStd',
                 'receiver': 'compact_oled_base.FCStd'}
    covers = {'sensor': 'PIRFrontCover', 'door': 'MagneticFrontCover',
              'receiver': 'BaseFrontCover'}
    doc = open_model(args.papaw_cad / 'output' / filenames[module])
    parts = []
    # Use printed parts from the current source document, not group compounds.
    for obj in doc.getObject('PrintableParts').Group:
        if obj.TypeId != 'Part::Feature' or obj.Shape.isNull(): continue
        is_cover = obj.Name == covers[module]
        offset = (-65 if module != 'receiver' else -43, 0, 0) if is_cover and exploded else None
        opacity = 1 if is_cover and exploded else (.18 if is_cover else .26)
        if 'MagnetPod' in obj.Name:
            opacity = .3
            offset = None
        parts.append((obj.Shape.copy(), (.68, .73, .77), opacity, offset))
    if module != 'receiver':
        prefix = 'PIR' if module == 'sensor' else 'MAG'
        retrofit = open_model(args.papaw_cad / 'aaa_retrofit' / 'output' /
                              f'{prefix}_installed_fit_REFERENCE.FCStd')
        for obj in retrofit.Objects:
            if obj.TypeId != 'Part::Feature' or obj.Name.startswith('Existing'): continue
            if obj.Shape.isNull(): continue
            parts.append((obj.Shape.copy(), battery_color(obj.Name), 1, None))
        parts += hardware.battery_details(6.75 if module == 'sensor' else 4.75)
        App.closeDocument(retrofit.Name)
    if module == 'sensor':
        parts += hardware.placed(hardware.esp32(), 37, 4, 42, quarter_turn=True)
        parts += hardware.placed(hardware.regulator(), 14, 17, 14)
        parts += hardware.placed(hardware.pir(), 3, 9, 43)
        wire_colors = {'PIR_VCC_Wire': (.7,.06,.04), 'PIR_OUT_Wire': (.8,.6,.08),
                       'PIR_GND_Wire': (.04,.045,.05)}
    elif module == 'door':
        parts += hardware.placed(hardware.esp32(), 3, 9.2, 41)
        parts += hardware.placed(hardware.regulator(), 3, 3, 42)
        parts += hardware.reed(50,17,41)
        parts.append((doc.getObject('MAG_Magnet').Shape.copy(), (.6,.64,.68), 1, None))
        wire_colors = {}
    else:
        parts += hardware.placed(hardware.esp32(), 5.25, 3.2, 3.4)
        parts += hardware.placed(hardware.oled(), 3.45, 10.3, 23.4)
        wire_colors = {'OLEDVCCWire': (.7,.06,.04), 'OLEDGNDWire': (.04,.045,.05),
                       'OLEDSDAWire': (.05,.3,.65), 'OLEDSCLWire': (.8,.6,.08)}
    for name, color in wire_colors.items():
        parts.append((doc.getObject(name).Shape.copy(), color, 1, None))
    App.closeDocument(doc.Name)
    return parts


if not args.only or args.only.startswith('papaw'):
    family = []
    for module, x in (('sensor', -85), ('door', 0), ('receiver', 85)):
        render(f'papaw-{module}-current.png', papaw_scene(module, True), (.9, 2.7, 1.15))
        family += [(s,c,o,(x,0,0)) for s,c,o,_ in papaw_scene(module, False)]
    render('papaw-family-current.png', family, (.4, 2.7, .9))
    provenance['papaw_components.py'] = hashlib.sha256(
        Path(hardware.__file__).read_bytes()).hexdigest()

if not args.only or args.only.startswith('xyz'):
    robot = open_model(args.xyz_cad / 'output' / 'XYZ_V34_Whole_Robot.FCStd')
    appearance = xyz_appearance.Appearance(args.xyz_cad, open_model)
    parts, wrist_parts = [], []
    for obj in robot.Objects:
        if not hasattr(obj, 'Package') or not hasattr(obj, 'Shape') or obj.Shape.isNull(): continue
        detailed = appearance.parts(obj)
        if obj.Package != 'routes' or obj.SourceKey.startswith('Upper_Braid_'):
            parts.extend(detailed)
        if obj.Package in ('wrist', 'camera', 'pen'):
            wrist_parts.extend(detailed)
    (args.review_dir / 'xyz-registration.json').write_text(
        json.dumps(appearance.errors, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(f'XYZ: {len(parts)} render parts; {len(appearance.errors)} registered components; '
          f'maximum registration error {max(appearance.errors.values()):.3g} mm', flush=True)
    render('xyz-robot-current.png', parts, (1.0, 1.5, .85))
    render('xyz-wrist-current.png', wrist_parts, (1.2, 1.7, .9))
    appearance.close()
    App.closeDocument(robot.Name)
    provenance['xyz_appearance.py'] = hashlib.sha256(
        Path(xyz_appearance.__file__).read_bytes()).hexdigest()
manifest = Path(__file__).with_name('render-sources.json')
previous = json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else {}
previous.update(provenance)
manifest.write_text(json.dumps(previous, indent=2) + '\n', encoding='utf-8', newline='\n')
