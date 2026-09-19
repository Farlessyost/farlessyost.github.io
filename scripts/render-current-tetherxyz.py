"""Export the current native scanner geometry for the portfolio."""
from pathlib import Path
import sys, math, subprocess, json
import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'XYZ Universal Medical Scanner/freecad/timber_frame_v39/simulation'
sys.path.insert(0, str(SOURCE))
from viewer import Viewer
FFMPEG = next((Path.home()/'.codex/tools/video-python/imageio_ffmpeg/binaries').glob('*.exe'))
v = Viewer(offscreen=True)
v.window.SetSize(960, 640)
v.window.SetMultiSamples(0)
def capture():
    v.window.Render()
    cap=vtk.vtkWindowToImageFilter(); cap.SetInput(v.window); cap.ReadFrontBufferOff(); cap.Update()
    arr=vtk_to_numpy(cap.GetOutput().GetPointData().GetScalars()).reshape(640,960,3)
    return np.flipud(arr).copy()
def clean_text():
    for r in (v.wide,v.close,v.guide):
        for a in list(r.GetActors2D()): a.SetVisibility(False)
clean_text()
v.t=v.data['home_time_s'];v.update();clean_text()
v.window.RemoveRenderer(v.close);v.window.RemoveRenderer(v.guide);v.wide.SetViewport(0,0,1,1)
frames=[]
for i in range(72):
    angle=2*math.pi*i/72
    v.camera(v.wide,(215.9+1700*math.sin(angle),177.8-1700*math.cos(angle),1000),(215.9,177.8,345),680)
    frame=Image.fromarray(capture())
    if i==0:frame.save(ROOT/'assets/images/tetherxyz-current-turntable.png')
    frames.append(frame)
frames[0].save(ROOT/'assets/images/tetherxyz-current-turntable.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=False)
print('Turntable complete',flush=True)
v.window.AddRenderer(v.close);v.window.AddRenderer(v.guide);v.wide.SetViewport(0,0,.62,1)
v.camera(v.wide,(550,-1600,900),(215.9,177.8,345),660)
fps=12
home=v.data['home_time_s'];end=v.data['duration_s']
times=list(np.arange(0,home,4/fps))+list(np.arange(home,end,24/fps))+[end]*36
out=ROOT/'assets/videos/tetherxyz-current-motion.mp4'
proc=subprocess.Popen([str(FFMPEG),'-y','-f','rawvideo','-pix_fmt','rgb24','-s','960x640','-r',str(fps),'-i','-','-an','-c:v','libx264','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',str(out)],stdin=subprocess.PIPE,stderr=subprocess.DEVNULL)
for i,t in enumerate(times):
    v.t=float(t);v.update();clean_text()
    v.title.SetInput('TetherXYZ | Homing and surface tracking');v.title.SetPosition(.025,.95);v.title.GetTextProperty().SetFontSize(16);v.title.SetVisibility(True)
    v.hud.SetInput(('Homing | 4x playback' if t<home else 'Surface tracking | 24x playback')+'\n'+v.status['label']);v.hud.GetTextProperty().SetFontSize(13);v.hud.SetVisibility(True)
    v.guide_title.SetVisibility(True);v.guide_title.GetTextProperty().SetFontSize(12)
    frame=capture();proc.stdin.write(frame.tobytes())
    if i==len(times)-1:Image.fromarray(frame).save(ROOT/'assets/images/tetherxyz-current-motion.png')
    if i%120==0:print(f'Motion {i}/{len(times)}',flush=True)
proc.stdin.close()
if proc.wait()!=0:raise RuntimeError('Video encoding failed')
(ROOT/'scripts/tetherxyz-current-media.json').write_text(json.dumps({'source':str(SOURCE),'turntable_frames':72,'motion_frames':len(times),'fps':fps,'duration_seconds':len(times)/fps,'homing_playback':4,'writing_playback':24},indent=2))
v.window.Finalize()
print('All exports complete',flush=True)
