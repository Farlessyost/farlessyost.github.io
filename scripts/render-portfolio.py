"""Export portfolio views from the saved engineering models, without UI overlays.

Run with FreeCAD's Python runtime; requires VTK. Source documents are read only.
"""
import argparse
import hashlib
import json
from pathlib import Path

import FreeCAD as App
import vtk

parser = argparse.ArgumentParser()
parser.add_argument('--papaw-cad', type=Path, required=True)
parser.add_argument('--xyz-cad', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--only', help='Render just this output filename')
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
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
    prop.SetAmbient(.25)
    prop.SetDiffuse(.75)
    prop.SetSpecular(.18)
    prop.SetSpecularPower(35)
    if offset:
        actor.SetPosition(*offset)
    return actor


def render(name, parts, direction, up=(0, 0, 1), zoom=1.1):
    if args.only and args.only != name:
        return
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(.953, .965, .977)
    renderer.SetUseDepthPeeling(True)
    renderer.SetMaximumNumberOfPeels(100)
    for shape, color, opacity, offset in parts:
        renderer.AddActor(actor_for(shape, color, opacity, offset))
    camera = renderer.GetActiveCamera()
    camera.SetPosition(*direction)
    camera.SetFocalPoint(0, 0, 0)
    camera.SetViewUp(*up)
    camera.ParallelProjectionOn()
    renderer.ResetCamera()
    camera.Zoom(zoom)
    window = vtk.vtkRenderWindow()
    window.SetOffScreenRendering(True)
    window.SetAlphaBitPlanes(True)
    window.SetMultiSamples(0)
    window.SetSize(1800, 1200)
    window.AddRenderer(renderer)
    window.Render()
    capture = vtk.vtkWindowToImageFilter()
    capture.SetInput(window)
    capture.Update()
    writer = vtk.vtkPNGWriter()
    writer.SetFileName(str(args.output / name))
    writer.SetInputConnection(capture.GetOutputPort())
    writer.Write()
    window.Finalize()
    print('Rendered ' + name, flush=True)


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
render('papaw-sensor-current.png', parts, (1.1, 1.6, 1.0), zoom=1.08)
App.closeDocument(pir.Name)
App.closeDocument(original.Name)

battery = open_model(retrofit / 'AAA_thin_frame_assembly_REFERENCE.FCStd')
parts = [(o.Shape, battery_color(o.Name), 1, None) for o in battery.Objects
         if hasattr(o, 'Shape') and not o.Shape.isNull()]
render('papaw-battery-current.png', parts, (1.1, 1.8, 1.3), zoom=1.1)
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
render('xyz-robot-current.png', parts, (1.0, 1.5, .85), zoom=.90)
render('xyz-wrist-current.png', wrist_parts, (1.2, 1.7, .9), zoom=1.08)
App.closeDocument(robot.Name)
(args.output.parent.parent / 'scripts' / 'render-sources.json').write_text(
    json.dumps(provenance, indent=2) + '\n', encoding='utf-8')
