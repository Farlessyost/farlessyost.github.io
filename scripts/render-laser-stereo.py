"""Export the current laser/stereo viewer without changing the running session."""
from pathlib import Path
import sys, subprocess, json, hashlib
import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'XYZ Universal Medical Scanner/freecad/laser_stereo_v43'
sys.path.insert(0,str(SOURCE))
from viewer import Viewer,G
v=Viewer(offscreen=True)
# Redirect automatic surface exports after the viewer has loaded its CAD files.
G.OUT=Path.home()/'Portfolio Renders/laser-stereo-website'
G.OUT.mkdir(parents=True,exist_ok=True)
width,height,fps=1560,980,12
v.window.SetSize(width,height)
for renderer in (v.wide,v.detail,v.reconstruction,v.left,v.right):
    for actor in list(renderer.GetActors2D()):
        if not hasattr(actor,'GetInput'):continue
        label=actor.GetInput()
        if 'Space pause' in label:actor.SetVisibility(False)
        elif label=='XYZ / LASER + STEREO':actor.SetInput('TetherXYZ | Laser + stereo')
        elif 'Native CAD head / synthetic' in label:actor.SetInput('30 mm camera baseline / Quarton line laser\nEleven overlapping sweeps over a raised surface')
        elif 'Synthetic laser-line image' in label:actor.SetInput('Laser-line image\n640 x 480 / ideal camera model')
        elif 'Height color uses' in label:actor.SetInput('Blue: baseline   Yellow/red: raised surface (0-10 mm)\nHeight relative to the modeled smooth arm')
ffmpeg=next((Path.home()/'.codex/tools/video-python/imageio_ffmpeg/binaries').glob('*.exe'))
out=ROOT/'assets/videos/tetherxyz-laser-stereo.mp4'
encoder=subprocess.Popen([str(ffmpeg),'-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{width}x{height}','-r',str(fps),'-i','-','-an','-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(out)],stdin=subprocess.PIPE)
count=int(np.ceil(G.PERIOD/G.PLAYBACK_SPEED*fps))
poster_frame=int((G.DURATION+G.HOLD/2)/G.PLAYBACK_SPEED*fps)
for i in range(count):
    v.elapsed=i/fps*G.PLAYBACK_SPEED;v.update()
    v.hud.SetInput(f'{v.status["stage"]}\n30 mm baseline / 11 sweeps / 3x playback\n{v.status["vertices"]:,} surface points / {v.status["triangles"]:,} triangles')
    v.window.Render()
    capture=vtk.vtkWindowToImageFilter();capture.SetInput(v.window);capture.ReadFrontBufferOff();capture.Update()
    pixels=np.flipud(vtk_to_numpy(capture.GetOutput().GetPointData().GetScalars()).reshape(height,width,3)).copy()
    encoder.stdin.write(pixels.tobytes())
    if i==poster_frame:Image.fromarray(pixels).save(ROOT/'assets/images/tetherxyz-laser-stereo.png')
    if i%100==0:print(f'Frame {i}/{count}',flush=True)
encoder.stdin.close()
if encoder.wait():raise RuntimeError('Video encoding failed')
(ROOT/'scripts/laser-stereo-media.json').write_text(json.dumps({'source':str(SOURCE),'source_sha256':{n:hashlib.sha256((SOURCE/n).read_bytes()).hexdigest() for n in ('viewer.py','design.py','scan.py')},'frames':count,'fps':fps,'duration_s':count/fps,'playback_speed':G.PLAYBACK_SPEED},indent=2))
v.window.Finalize()
print('Laser/stereo video exported',flush=True)
