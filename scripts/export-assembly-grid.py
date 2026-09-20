"""Export four CAD assembly views through FreeCAD Render/LuxCore."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(Path.home()/'Portfolio Renders/2026-09-14'))
import render_previews as S
CAD=ROOT.parent/'XYZ Universal Medical Scanner/freecad/structural_v54/output/XYZ_V54_Serviceable_Scanner.FCStd'
DEST=Path.home()/'Portfolio Renders/tetherxyz-four-assemblies'
doc=S.open_model(CAD)
objects=[o for o in doc.Objects if hasattr(o,'Shape') and o.Shape.Solids and hasattr(o,'Category')]
def pod(o):return o.Name.startswith('Pod_1_')
def wrist(o):return o.Name.startswith('Retained_Wrist_')
def has(o,*words):return any(w in o.Name for w in words)
groups=[
('Winch assembly',pod),
('Two-DOF arm',wrist),
('Rod and guide',lambda o:o.Name.startswith('Compact_') or o.Group=='rod'),
('Stereo and laser',lambda o:o.Name.startswith('LaserStereo_')),
]

parts=[];ids=[];layout=[]
# Camera-facing tile coordinates, retaining an oblique view of each subsystem.
view=np.array([1.,-1.5,.85]);view/=np.linalg.norm(view)
right=np.cross([0,0,1],view);right/=np.linalg.norm(right)
up=np.cross(view,right);orient=np.array([right,up,view])
for i,(title,select) in enumerate(groups):
    selected=[o for o in objects if select(o)]
    assert len(selected)>1,(title,len(selected))
    bounds=S.App.BoundBox()
    for o in selected:bounds.add(o.Shape.BoundBox)
    center=np.array(list(bounds.Center));radius=np.linalg.norm([bounds.XLength,bounds.YLength,bounds.ZLength])/2
    scale=285/radius
    tile=np.array([(i%2-.5)*1000,(.5-i//2)*1000,0.])
    entries=[]
    for o in selected:
        shape=o.Shape.copy();partcenter=np.array(list(shape.BoundBox.Center))
        # Radial separation preserves each component's orientation and identity.
        delta=orient@(partcenter-center)*scale*.65
        transform=S.App.Matrix()
        for a in range(3):
            for b in range(3):setattr(transform,f'A{a+1}{b+1}',float(orient[a,b]*scale))
            setattr(transform,f'A{a+1}4',float(tile[a]-(orient@center)[a]*scale))
        shape.transformShape(transform)
        color=tuple(o.RenderColor)[:3];name=o.Name.lower();finish='plastic'
        if o.Category=='timber':finish='wood'
        elif o.Category in ('buy','hardware','fabricate') and not any(x in name for x in ('servo_envelope','motor_envelope','pcb','board')):finish='metal'
        elif 'lens_glass' in name:finish='glass'
        elif max(color)<.15:finish='rubber'
        identifier=f'{i:02d}:{o.Name}'
        parts.append((shape,color,1,None,finish));ids.append(identifier)
        entries.append({'id':identifier,'name':o.Name,'delta':(delta*.001).tolist()})
    layout.append({'title':title,'center':(tile*.001).tolist(),'parts':entries})
    print(title,len(selected),flush=True)
directory,template=S.export_scene('grid',parts,(.001,0,1),1280,1280,component_ids=ids,scene_root=DEST)
S.App.closeDocument(doc.Name)
params=S.App.ParamGet('User parameter:BaseApp/Preferences/Mod/Render');params.SetInt('LuxCoreEngine',0)
params.SetString('LuxCoreConsolePath',str(S.ENGINE/'bin/luxcoreconsole.exe'))
S.Luxcore.render(S.types.SimpleNamespace(Name='grid'),'',True,str(template),str(directory/'grid.png'),1280,1280,24,True)
cfg=directory/'grid.cfg';cfg.write_text(cfg.read_text().replace('film.imagepipelines.0.99.value = 1.8','film.imagepipelines.0.99.value = 2.2'))
(DEST/'layout.json').write_text(json.dumps({'cad':str(CAD),'sha256':hashlib.sha256(CAD.read_bytes()).hexdigest(),'orientation':orient.tolist(),'tiles':layout},indent=2))
print('Grid export complete',flush=True)
