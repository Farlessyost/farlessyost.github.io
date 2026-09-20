"""Ray-trace four synchronized assembly turntables and exploded views.

After export-assembly-grid.py, run this script normally, with --head, then
with --encode-only to combine the lens-facing optical view and encode media.
"""
from pathlib import Path
import sys,json,math,time,os,subprocess,re
sys.path.insert(0,str(Path.home()/'.codex/tools/python39-luxcore/Lib/site-packages'))
import numpy as np
from PIL import Image,ImageDraw,ImageFont
sys.path.insert(0,str(Path.home()/'Portfolio Renders/2026-09-14'))
import render_turntables as R
L=R.lux
ROOT=Path(__file__).resolve().parents[1]
DEST=Path.home()/'Portfolio Renders/tetherxyz-four-assemblies'
head_only='--head' in sys.argv
source=DEST/'grid';frames=DEST/('head-tilt-frames' if head_only else 'final-frames');frames.mkdir(exist_ok=True)
data=json.loads((DEST/'layout.json').read_text());layout=json.loads((source/'component-layout.json').read_text())
for tile in data['tiles']:tile['title']=tile['title'].replace('Two-axis wrist','Two-DOF arm')
orient=np.array(data['orientation']);lookup={p['id']:(tile,p) for tile in data['tiles'] for p in tile['parts']}
width=640 if head_only else 1280;spin=32;explode=10;samples=24
preview='--preview' in sys.argv
log=(DEST/'render.log').open('w');L.Init(lambda s:log.write(s+'\n'))
scene_text='\n'.join(line for line in (source/'grid.scn').read_text().splitlines() if not line.startswith('scene.objects.studio_floor.'))
if head_only:
    allowed={name for name,item in layout.items() if lookup[item['component']][0] is data['tiles'][3]}
    def keep(line):
        match=re.search(r'part\d+_(?:plastic|metal|rubber|glass)',line)
        return not match or match[0] in allowed
    scene_text='\n'.join(line for line in scene_text.splitlines() if keep(line))
props=L.Properties();props.SetFromString(scene_text)
for key,value in {'scene.camera.lookat.orig':[0,0,30],'scene.camera.lookat.target':[0,0,0],'scene.camera.up':[0,1,0],'scene.camera.fieldofview':math.degrees(2*math.atan(1/30)),'scene.lights.ambient.color':[.015,.018,.025]}.items():R.property_set(props,key,value)
scene=L.Scene(props)
# Optical outward normal at the CAD's saved scan pose, from optical_world().
normal=np.array([0.,-.7592566023652965,-.6507913734559684])
target=orient[2];axis=np.cross(normal,target);cosine=float(normal@target)
cross=np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
align=np.eye(3)+cross+cross@cross/(1+cosine)
flip=orient@align@orient.T
if head_only:
    camera=scene.ToProperties().GetAllProperties('scene.camera')
    for key,value in {'scene.camera.lookat.orig':[.5,-.5,30],'scene.camera.lookat.target':[.5,-.5,0],'scene.camera.fieldofview':math.degrees(2*math.atan(.5/30))}.items():R.property_set(camera,key,value)
    scene.Parse(camera)
config=L.Properties(str(source/'grid.cfg'))
for key,value in {'renderengine.type':'PATHCPU','film.width':width,'film.height':width,'batch.haltspp':samples,'film.noiseestimation.warmup':samples,'native.threads.count':4 if head_only and '--fast' not in sys.argv else 12,'film.opencl.enable':False,'film.hw.enable':False,'periodicsave.film.outputs.period':-1,'renderengine.seed':1}.items():R.property_set(config,key,value)
session=L.RenderSession(L.RenderConfig(config,scene));session.Start()
import itertools
fit={}
for tile in data['tiles']:
    center=np.array(tile['center']);points=[]
    for name,item in layout.items():
        owner,part=lookup[item['component']]
        if owner is not tile:continue
        b=item['bounds'];corners=np.array(list(itertools.product(*zip(b[:3],b[3:]))))
        points.extend(corners-center+np.array(part['delta'])*1.7)
    if head_only and tile is data['tiles'][3]:points=np.array(points)@flip.T
    span=np.abs(points).max(0)
    fit[tile['title']]=min(1.25,.42/span[0],.39/span[1])
font=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf',28)
jobs=[('spin',i) for i in range(spin)]+[('explode',i) for i in range(explode)]
if preview:jobs=[('spin',0),('explode',explode-1)]
if '--encode-only' in sys.argv:jobs=[]
try:
 for phase,index in jobs:
    target=frames/f'{phase}-{index:03d}.png'
    if target.exists():continue
    start=time.monotonic();session.BeginSceneEdit()
    theta=2*math.pi*index/spin if phase=='spin' else 0
    c,s=math.cos(theta),math.sin(theta);rotation=orient@np.array([[c,-s,0],[s,c,0],[0,0,1]])@orient.T
    u=(index+1)/explode if phase=='explode' else 0;amount=u*u*(3-2*u)
    angle=math.radians(35)*amount;ct,st=math.cos(angle),math.sin(angle)
    tilted=np.array([[ct,0,st],[0,1,0],[-st,0,ct]])@flip
    head_zoom=1.25
    if head_only:
        points=[];center=np.array(data['tiles'][3]['center'])
        for item in layout.values():
            tile,part=lookup[item['component']]
            if tile is not data['tiles'][3]:continue
            b=item['bounds'];corners=np.array(list(itertools.product(*zip(b[:3],b[3:]))))
            points.extend((corners-center+np.array(part['delta'])*amount*1.7)@tilted.T)
        span=np.abs(points).max(0);head_zoom=min(1.25,.42/span[0],.39/span[1])
    for name,item in layout.items():
        tile,part=lookup[item['component']];center=np.array(tile['center'])
        if head_only and tile is not data['tiles'][3]:continue
        zoom=1.25+(fit[tile['title']]-1.25)*amount
        if head_only and phase=='explode':zoom=head_zoom
        local_rotation=rotation@tilted if head_only and tile is data['tiles'][3] else rotation
        delta=tilted@np.array(part['delta']) if head_only and tile is data['tiles'][3] else np.array(part['delta'])
        m=np.eye(4);m[:3,:3]=local_rotation*zoom;m[:3,3]=center-zoom*local_rotation@center+zoom*delta*amount*1.7+[0,-.025,0]
        scene.UpdateObjectTransformation(name,m.T.flatten().tolist())
    session.EndSceneEdit();session.UpdateStats()
    while not session.HasDone():time.sleep(.1);session.UpdateStats()
    session.GetFilm().SaveOutput(str(target),L.FilmOutputType.RGB_IMAGEPIPELINE,L.Properties())
    image=Image.open(target).convert('RGB');draw=ImageDraw.Draw(image)
    for i,tile in enumerate(data['tiles']):
        if head_only and i!=3:continue
        x=0 if head_only else i%2*640;y=0 if head_only else i//2*640
        draw.rectangle((x,y,x+639,y+48),fill=(27,31,36))
        draw.text((x+14,y+8),f'{i+1:02d}  {tile["title"]}',font=font,fill=(235,237,239))
        draw.line((x,y+639,x+639,y+639),fill=(70,76,83),width=1)
        draw.line((x+639,y,x+639,y+639),fill=(70,76,83),width=1)
    image.save(target)
    print(f'{phase} {index+1}: {time.monotonic()-start:.1f}s',flush=True)
finally:session.Stop();log.flush()
if head_only:
 print('Optical module views complete',flush=True)
 sys.stdout.flush();os._exit(0)
if not preview:
 if '--encode-only' in sys.argv:
    for phase,index in [('spin',i) for i in range(spin)]+[('explode',i) for i in range(explode)]:
        path=frames/f'{phase}-{index:03d}.png';image=Image.open(path).convert('RGB')
        head=Image.open(DEST/'head-tilt-frames'/path.name);image.paste(head,(640,640));image.save(path)
 timeline=[frames/f'spin-{i:03d}.png' for i in range(spin)]+[frames/'spin-000.png']*4+[frames/f'explode-{i:03d}.png' for i in range(explode)]+[frames/f'explode-{explode-1:03d}.png']*8+[frames/f'explode-{i:03d}.png' for i in range(explode-2,-1,-1)]+[frames/'spin-000.png']*4
 temp=DEST/'timeline';temp.mkdir(exist_ok=True)
 import shutil
 for i,p in enumerate(timeline):shutil.copyfile(p,temp/f'{i:04d}.png')
 gif=ROOT/'assets/images/tetherxyz-assembly-grid.gif';mp4=ROOT/'assets/videos/tetherxyz-assembly-grid.mp4'
 cmd=[str(R.FFMPEG),'-y','-loglevel','error','-framerate','8','-i',str(temp/'%04d.png')]
 subprocess.run(cmd+['-filter_complex','[0:v]split[a][b];[a]palettegen[p];[b][p]paletteuse=dither=none','-loop','0',str(gif)],check=True)
 subprocess.run(cmd+['-c:v','libx264','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart',str(mp4)],check=True)
 shutil.copyfile(frames/'spin-000.png',ROOT/'assets/images/tetherxyz-assembly-grid.png')
 (ROOT/'scripts/assembly-grid-media.json').write_text(json.dumps({'cad':data['cad'],'cad_sha256':data['sha256'],'engine':'FreeCAD Render / LuxCore PATHCPU','samples':samples,'size':[width,width],'frames':len(timeline),'fps':8,'grid':[2,2],'optical_view':'Lens-facing orientation' if '--encode-only' in sys.argv else 'Assembly orientation','tiles':[{'title':t['title'],'parts':[p['name'] for p in t['parts']]} for t in data['tiles']]},indent=2))
 print('Grid GIF and video complete',flush=True)
sys.stdout.flush();os._exit(0)
