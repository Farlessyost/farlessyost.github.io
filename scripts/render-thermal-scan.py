"""Export the existing temperature-scan simulation for the portfolio."""
from pathlib import Path
import sys, subprocess, json, hashlib
import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'XYZ Universal Medical Scanner/freecad/thermal_scanner_v41'
sys.path.insert(0,str(SOURCE))
from viewer import Viewer,T
review=Path.home()/'Portfolio Renders/thermal-website'
review.mkdir(parents=True,exist_ok=True)
T.OUT=review
v=Viewer(offscreen=True)
width,height,fps=1200,752,16
v.window.SetSize(width,height)
# Keep useful labels and remove desktop keyboard instructions from the video.
for renderer in (v.wide,v.detail,v.live):
    for actor in list(renderer.GetActors2D()):
        if not hasattr(actor,'GetInput'):continue
        text=actor.GetInput()
        if 'Space:' in text:actor.SetVisibility(False)
        elif text=='XYZ / THERMAL SCAN':actor.SetInput('TetherXYZ | Temperature scan')
        elif 'Adafruit MLX90640 / #4407' in text:actor.SetInput('MLX90640 | 32 x 24 pixels\nScan, hold, and return')
        elif 'Fixed scale / synthetic' in text:actor.SetInput('30 C   blue > teal > yellow > red > pale   37 C')
        elif 'Colors appear only' in text:actor.SetInput('Temperature map built from the acquired samples')
        actor.GetTextProperty().SetFontSize(round(actor.GetTextProperty().GetFontSize()*.8))
ffmpeg=next((Path.home()/'.codex/tools/video-python/imageio_ffmpeg/binaries').glob('*.exe'))
out=ROOT/'assets/videos/tetherxyz-temperature-scan.mp4'
encoder=subprocess.Popen([str(ffmpeg),'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{width}x{height}','-r',str(fps),'-i','-','-an','-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(out)],stdin=subprocess.PIPE)
count=int(np.ceil(T.PERIOD*fps))
for i in range(count):
    v.elapsed=i/fps;v.update()
    v.hud.SetInput(f'{v.status["stage"].capitalize()}\n45 mm clearance | 12 mm/s\n{len(v.scan.records)} sensor frames acquired')
    v.live_stats.SetInput(v.live_stats.GetInput().split(' | ')[0])
    v.window.Render()
    capture=vtk.vtkWindowToImageFilter();capture.SetInput(v.window);capture.ReadFrontBufferOff();capture.Update()
    pixels=np.flipud(vtk_to_numpy(capture.GetOutput().GetPointData().GetScalars()).reshape(height,width,3)).copy()
    encoder.stdin.write(pixels.tobytes())
    if i==int((T.DURATION+1)*fps):Image.fromarray(pixels).save(ROOT/'assets/images/tetherxyz-temperature-scan.png')
    if i%100==0:print(f'Frame {i}/{count}',flush=True)
encoder.stdin.close()
if encoder.wait():raise RuntimeError('Video encoding failed')
(ROOT/'scripts/thermal-scan-media.json').write_text(json.dumps({'source':str(SOURCE),'source_sha256':{n:hashlib.sha256((SOURCE/n).read_bytes()).hexdigest() for n in ('viewer.py','thermal.py')},'frames':count,'fps':fps,'duration_s':count/fps,'temperature_data':'Modeled temperature field'},indent=2))
v.window.Finalize()
print('Thermal video exported',flush=True)
