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

parser = argparse.ArgumentParser()
parser.add_argument('--papaw-cad', type=Path, required=True)
parser.add_argument('--xyz-cad', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--only', help='Render just this output filename')
parser.add_argument('--ffmpeg', required=True, type=Path)
parser.add_argument('--review-dir', required=True, type=Path)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
args.review_dir.mkdir(parents=True, exist_ok=True)
provenance = {}


def open_model(path):
    provenance[path.name] = hashlib.sha256(path.read_bytes()).hexdigest()
    return App.openDocument(str(path))


def actor_for(shape, color, opacity=1, offset=None):
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
    if offset:
        actor.SetPosition(*offset)
    return actor


def render(name, parts, direction, up=(0, 0, 1)):
    if args.only and args.only != name:
        return
    width, height, frames, fps = 960, 640, 120, 12.5
    renderer = vtk.vtkRenderer()
    # Match the owner's FreeCAD viewport color (#1f1f1f).
    renderer.SetBackground(31 / 255, 31 / 255, 31 / 255)
    renderer.SetUseDepthPeeling(True)
    renderer.SetMaximumNumberOfPeels(100)
    renderer.SetUseFXAA(True)
    corners = []
    for shape, color, opacity, offset in parts:
        actor = actor_for(shape, color, opacity, offset)
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
    log_path = args.review_dir / (gif.stem + '.log')
    command = [str(args.ffmpeg), '-y', '-loglevel', 'error', '-f', 'rawvideo',
               '-pixel_format', 'rgb24', '-video_size', f'{width}x{height}',
               '-framerate', str(fps), '-i', 'pipe:0', '-filter_complex',
               '[0:v]split[a][b];[a]palettegen=stats_mode=full[p];'
               '[b][p]paletteuse=dither=bayer:bayer_scale=3:diff_mode=rectangle',
               '-loop', '0', str(gif)]
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
                    Image.fromarray(pixels).save(args.output / name)
                if i % (frames // 4) == 0:
                    Image.fromarray(pixels).save(args.review_dir / f'{gif.stem}-{i:03d}.png')
                encoder.stdin.write(pixels.tobytes())
                camera.Azimuth(360 / frames)
                if (i + 1) % 30 == 0:
                    print(f'{gif.name}: {i + 1}/{frames} frames', flush=True)
            encoder.stdin.close()
            if encoder.wait() != 0:
                raise RuntimeError(log_path.read_text())
        finally:
            if encoder.poll() is None:
                encoder.kill()
            window.Finalize()
    print(f'Rendered {gif.name}: {gif.stat().st_size:,} bytes', flush=True)


def battery_color(name):
    if 'frame' in name.lower(): return (.09, .52, .52)
    if 'cells' in name.lower(): return (.23, .39, .62)
    if 'leaves' in name.lower(): return (.76, .65, .39)
    if 'Positive' in name: return (.76, .12, .10)
    if 'Joint' in name: return (.60, .64, .68)
    return (.12, .16, .20)


retrofit = args.papaw_cad / 'aaa_retrofit' / 'output'
pir = open_model(retrofit / 'PIR_installed_fit_REFERENCE.FCStd')
original = open_model(args.papaw_cad / 'output' / 'compact_pir_node.FCStd')
parts = []
for obj in pir.Objects:
    if not hasattr(obj, 'Shape') or obj.Shape.isNull(): continue
    color, opacity = battery_color(obj.Name), 1
    if obj.Name == 'ExistingRearShell': color, opacity = (.57, .64, .70), .22
    if obj.Name == 'ExistingElectronics': color = (.12, .32, .24)
    parts.append((obj.Shape, color, opacity, None))
parts.append((original.getObject('PIRFrontCover').Shape, (.72, .77, .81), 1, (0, 30, 0)))
render('papaw-sensor-current.png', parts, (1.1, 1.6, 1.0))
App.closeDocument(pir.Name)
App.closeDocument(original.Name)

battery = open_model(retrofit / 'AAA_thin_frame_assembly_REFERENCE.FCStd')
parts = [(o.Shape, battery_color(o.Name), 1, None) for o in battery.Objects
         if hasattr(o, 'Shape') and not o.Shape.isNull()]
render('papaw-battery-current.png', parts, (1.1, 1.8, 1.3))
App.closeDocument(battery.Name)

robot = open_model(args.xyz_cad / 'output' / 'XYZ_V34_Whole_Robot.FCStd')
parts, wrist_parts = [], []
for obj in robot.Objects:
    if not hasattr(obj, 'Package') or not hasattr(obj, 'Shape') or obj.Shape.isNull(): continue
    color = tuple(obj.RenderColor)[:3]
    part = (obj.Shape, color, 1, None)
    if obj.Package != 'routes' or obj.SourceKey.startswith('Upper_Braid_'):
        parts.append(part)
    if obj.Package in ('wrist', 'camera', 'pen'):
        wrist_parts.append(part)
render('xyz-robot-current.png', parts, (1.0, 1.5, .85))
render('xyz-wrist-current.png', wrist_parts, (1.2, 1.7, .9))
App.closeDocument(robot.Name)
(args.output.parent.parent / 'scripts' / 'render-sources.json').write_text(
    json.dumps(provenance, indent=2) + '\n', encoding='utf-8', newline='\n')
