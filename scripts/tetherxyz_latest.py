"""Read-only adapter from the structural CAD revision to the optical viewer."""
from pathlib import Path
import json, sys
import numpy as np
import vtk
from vtk.util.numpy_support import numpy_to_vtk

CAD = Path(__file__).resolve().parents[2]/'XYZ Universal Medical Scanner/freecad/structural_v54/output'
OPTICS = CAD.parents[1]/'laser_stereo_v53'
sys.path.insert(0,str(OPTICS))
from viewer import Viewer,G
INSTALL=json.loads((CAD/'installation.json').read_text())

def evaluate(offsets,state):
    frames=G.M.D.BASE.frames(state)
    routes=[G.M.R.route(lug,pod,radius=18) for lug,pod in zip(G.M.D.lugs(state),INSTALL['pods'])]
    for i,(pod,route) in enumerate(zip(INSTALL['pods'],routes)):
        frames[f'pod_{i}_fixed']=(np.array(pod['rotation_world_from_pod']),np.array(pod['origin_world_mm']))
        frames[f'pod_{i}_swivel']=(np.array(route['swivel_rotation_world']),np.array(route['swivel_translation_world_mm']))
        frames[f'pod_{i}_wheel']=frames[f'pod_{i}_swivel']
    return {'frames':frames,'routes':routes}

def create_viewer():
    G.M.evaluate=evaluate
    v=Viewer(offscreen=True)
    for _,actor in v.actors:
        v.wide.RemoveActor(actor);v.detail.RemoveActor(actor)
    v.actors=[]
    saved=evaluate(None,G.pose(G.DURATION*.55))['frames']
    for item in json.loads((CAD/'meshes.json').read_text()):
        # Timber remains in the CAD renders; keep the scanning view unobstructed.
        if item['category']=='timber' or item['name'].startswith('Mount_Pod_'):continue
        group=item['group'];r,t=saved.get(group,(np.eye(3),np.zeros(3)))
        points=(np.array(item['vertices'])-t)@r
        p=vtk.vtkPoints();p.SetData(numpy_to_vtk(points,deep=True));cells=vtk.vtkCellArray()
        for face in item['faces']:
            cells.InsertNextCell(3)
            for index in face:cells.InsertCellPoint(index)
        poly=vtk.vtkPolyData();poly.SetPoints(p);poly.SetPolys(cells)
        normals=vtk.vtkPolyDataNormals();normals.SetInputData(poly);normals.SetFeatureAngle(45)
        mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(normals.GetOutputPort())
        actor=vtk.vtkActor();actor.SetMapper(mapper);actor.GetProperty().SetColor(*item['color'][:3])
        v.wide.AddActor(actor)
        if group.startswith('wrist') or group=='head' or item['name']=='Unified_Arm_Skin' or item['name'].endswith('_Nail'):v.detail.AddActor(actor)
        v.actors.append((group,actor))
    # Some fixed reference bodies have no explicit entry in the motion model.
    original=evaluate
    def with_fixed(offsets,state):
        result=original(offsets,state)
        for group,_ in v.actors:result['frames'].setdefault(group,(np.eye(3),np.zeros(3)))
        return result
    G.M.evaluate=with_fixed
    v.scan.export=lambda:None
    v.update()
    return v
