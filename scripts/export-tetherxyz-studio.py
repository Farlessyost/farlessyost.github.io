"""Export the current CAD with the portfolio's original FreeCAD/LuxCore studio."""
import sys, json, hashlib
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PREVIOUS = Path.home() / 'Portfolio Renders/2026-09-14'
DEST = Path.home() / 'Portfolio Renders/tetherxyz-current-studio'
sys.path.insert(0, str(PREVIOUS))
import render_previews as studio

source = REPO.parent/'XYZ Universal Medical Scanner/freecad/timber_frame_v39/output/XYZ_V39_Flat_Swivel_Scanner.FCStd'
doc = studio.open_model(source)
parts=[]
for obj in doc.Objects:
    if not hasattr(obj,'Package') or not hasattr(obj,'Shape') or obj.Shape.isNull(): continue
    name=obj.Name.lower(); package=obj.Package
    color=tuple(obj.RenderColor)[:3]
    finish='plastic'
    if package=='support_context':
        finish='metal' if 'table_leg' in name else 'wood'
    elif package in ('mount_hardware','stock') or any(x in name for x in ('bolt','washer','nut','bearing','shaft','screw','pin_','steel','threaded','axle')):
        finish='metal'
    elif package=='cable': finish='rubber';color=(.12,.16,.17)
    elif any(x in name for x in ('lens','glass')):finish='glass'
    elif max(color)<.15:finish='rubber'
    parts.append((obj.Shape.copy(),color,1,None,finish))
directory,template=studio.export_scene('xyz-machine',parts,(1,-1.5,.85),960,640,scene_root=DEST)
studio.App.closeDocument(doc.Name)
# Use the workbench exporter to generate the same render pipeline as before.
params=studio.App.ParamGet('User parameter:BaseApp/Preferences/Mod/Render')
params.SetInt('LuxCoreEngine',0)
params.SetString('LuxCoreConsolePath',str(studio.ENGINE/'bin/luxcoreconsole.exe'))
studio.Luxcore.render(studio.types.SimpleNamespace(Name='xyz-machine'),'',True,str(template),str(directory/'xyz-machine.png'),960,640,32,True)
cfg=directory/'xyz-machine.cfg'
cfg.write_text(cfg.read_text().replace('film.imagepipelines.0.99.value = 1.8','film.imagepipelines.0.99.value = 2.2'))
(DEST/'source.json').write_text(json.dumps({'cad':str(source),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'parts':len(parts),'studio':str(PREVIOUS)},indent=2))
print('Studio export complete:',directory,flush=True)
