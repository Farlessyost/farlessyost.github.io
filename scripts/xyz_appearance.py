"""Presentation details for the existing XYZ assembly.

These approximate small purchased-component details; they do not change the
engineering source documents or qualify physical fit. See xyz-render-notes.md.
"""
import json
import math
from functools import lru_cache

import numpy as np
import FreeCAD as App
import Part
import vtk
from vtk.util.numpy_support import numpy_to_vtk
import papaw_components as H

V = App.Vector
STEEL = (.66, .70, .74)
BLACK = (.035, .04, .048)
SERVO_BLUE = (.035, .14, .56)


def box(x,y,z,w,d,h):
    return Part.makeBox(w,d,h,V(x,y,z))


def cyl(x,y,z,r,h):
    return Part.makeCylinder(r,h,V(x,y,z))


def record(shape, color, finish='plastic', opacity=1):
    return (shape,color,opacity,None,finish)


def transform(shape, rotation, translation):
    matrix=App.Matrix()
    for i in range(3):
        for j in range(3):setattr(matrix,f'A{i+1}{j+1}',float(rotation[i,j]))
        setattr(matrix,f'A{i+1}4',float(translation[i]))
    result=shape.copy();result.transformShape(matrix,True)
    return result


def register(source, target):
    """Recover the saved assembly transform, rejecting a mismatched source."""
    a=np.array([[v.Point.x,v.Point.y,v.Point.z] for v in source.Vertexes])
    b=np.array([[v.Point.x,v.Point.y,v.Point.z] for v in target.Vertexes])
    if a.shape != b.shape:raise ValueError('Component source topology changed')
    ac,bc=a.mean(0),b.mean(0)
    u,_,vh=np.linalg.svd((a-ac).T@(b-bc))
    r=vh.T@u.T
    if np.linalg.det(r)<0:vh[-1]*=-1;r=vh.T@u.T
    t=bc-r@ac
    error=np.max(np.linalg.norm(a@r.T+t-b,axis=1))
    if error>1e-5:raise ValueError(f'Component registration error: {error:.6f} mm')
    return r,t,float(error)


def side_label(text,u,v,a,size,direction=1,color=BLACK):
    parts=[];H.label(parts,text,0,0,0,size,color)
    s=parts[0][0]
    s.rotate(V(),V(0,0,1),-90*direction)
    s.translate(V(u,v,a))
    return record(s,color)


@lru_cache(maxsize=1)
def servo():
    """SG90-style case in the native drive's u/v/axial coordinates."""
    parts=[]
    # Distinct bottom lid, body, ear flange, gearbox lid and output boss.
    for z,h,color in ((20.1,14.6,SERVO_BLUE),(34.85,2.15,(.025,.095,.36)),
                      (14.15,3.85,(.045,.19,.66))):
        parts.append(record(box(38.9,-6,z,12.2,22.7,h),color))
    ears=box(38.9,-10.8,18,12.2,32.3,2)
    for vv in (-8.65,19.35):ears=ears.cut(cyl(45,vv,17.9,1.15,2.2))
    parts.append(record(ears,(.04,.16,.61)))
    # Rounded gearbox towers replace the former solid rectangular top.
    gear=cyl(45,0,10,5.9,4).fuse(cyl(45,7.1,11,3.65,3))
    parts.append(record(gear,(.04,.18,.63)))
    for x in (40.1,49.9):
        for y in (-4.8,15.5):
            head=cyl(x,y,36.8,.75,.27)
            slot=box(x-.12,y-.65,36.95,.24,1.3,.3)
            parts.append(record(head.cut(slot),(.20,.23,.27),'metal'))
    for direction,u in ((1,51.12),(-1,38.82)):
        parts.append(record(box(u,-2.65,24,.06,16,8.3),(.82,.85,.87)))
        parts.append(side_label('SG90',u+.065 if direction==1 else u-.015,5.35,28.2,2.15,direction))
        parts.append(side_label('9g SERVO',u+.065 if direction==1 else u-.015,5.35,25.4,1.05,direction))
    parts.append(record(box(43.2,3.55,36.6,3.6,3.6,1.9),BLACK,'rubber'))
    # Three short flexible lead tails with the usual signal/power/ground colors.
    for i,color in enumerate(((.59,.22,.045),(.67,.045,.025),(.13,.055,.025))):
        points=[V(44.1+i*.85,5.3,37.5),V(44.1+i*.85,5.3,42),
                V(45+i*.85,7,47),V(48+i*.85,10,50)]
        pieces=[]
        for a,b in zip(points,points[1:]):
            delta=b-a;pieces.append(Part.makeCylinder(.34,delta.Length,a,delta))
        pieces.extend(Part.makeSphere(.34,p) for p in points[1:-1])
        parts.append(record(Part.makeCompound(pieces),color,'rubber'))
    return parts


def optical(shape):
    f=math.hypot(35,30)
    r=np.array([[1,0,0],[0,30/f,35/f],[0,-35/f,30/f]])
    return transform(shape,r,np.array([0,35,-30]))


def camera_board(z):
    parts=[]
    pcb=box(-46.25,-3.5,z,40.5,27,1.6)
    for x in (-44.6,-7.4):
        for y in (-1.85,21.85):pcb=pcb.cut(cyl(x,y,z-.1,.7,1.8))
    parts.append(record(pcb,(.03,.16,.09)))
    # Plated header holes, smaller passives and the optical-side flex connector.
    pads=[]
    for y in (-1.43,21.43):
        for i in range(8):
            x=-34.9+i*2.54
            pads.append(cyl(x,y,z+1.6,.75,.04).cut(cyl(x,y,z+1.59,.34,.08)))
    parts.append(record(Part.makeCompound(pads),H.GOLD,'metal'))
    for x,y in ((-43,4),(-39,4),(-42,8),(-38,16),(-14,18),(-10,17),(-11,3)):
        parts.append(record(box(x,y,z-.62,1.6,.8,.6),(.5,.4,.26)))
        parts.append(record(box(x-.07,y,z-.65,.3,.8,.65),STEEL,'metal'))
        parts.append(record(box(x+1.37,y,z-.65,.3,.8,.65),STEEL,'metal'))
    parts.append(record(box(-43,8,z-1.3,5.5,4,1.3),BLACK))
    parts.append(record(box(-44,11,z-2.2,3,11,2.2),(.73,.73,.66)))
    parts.append(record(box(-44.1,11,z-2.3,.5,11,.45),BLACK))
    parts.append(record(box(-10.5,-.2,z-1.1,2,1.6,1.1),(.78,.80,.64)))
    return parts


def camera_header(y,z):
    parts=[record(box(-34.9-1.27,y-1.27,z+1.6,20.32,2.54,2.5),BLACK)]
    pins=[box(-34.9+i*2.54-.32,y-.32,z+1.2,.64,.64,8.8) for i in range(8)]
    parts.append(record(Part.makeCompound(pins),H.GOLD,'metal'))
    return parts


def camera_shield(z):
    # ESP module carrier, stamped shield can, seam and exposed antenna end.
    parts=[record(box(-35,2,z+1.6,18,16,.8),BLACK)]
    shell=box(-34.65,2.3,z+2.4,17.3,10.5,1.55)
    shell=shell.cut(box(-34.4,2.55,z+2.39,16.8,10,.95))
    parts.append(record(shell,STEEL,'metal'))
    traces=[]
    for i in range(4):
        traces.append(box(-32.5+i*3.5,13.3,z+2.41,.55,3.1,.025))
        traces.append(box(-32.5+i*3.5,15.9 if i%2==0 else 13.3,z+2.41,3.5,.5,.025))
    parts.append(record(Part.makeCompound(traces),H.GOLD,'metal'))
    return parts


def sd_socket(z):
    outer=box(-20.5,2.5,z-1.6,14,15,1.6)
    cavity=box(-20.2,2.3,z-1.35,13.4,14.8,.95)
    slot=box(-19,4,z-1.65,3,2,.3)
    parts=[record(outer.cut(cavity).cut(slot),STEEL,'metal')]
    for i in range(8):parts.append(record(box(-19+i*1.45,15.8,z-1.05,.55,1.5,.22),H.GOLD,'metal'))
    return parts


def lens(x):
    parts=[]
    barrel=cyl(x,0,0,3.7,5).cut(cyl(x,0,-.1,2.75,5.2))
    for z in (.6,1.4,2.2,3.0):
        groove=cyl(x,0,z,3.8,.17).cut(cyl(x,0,z-.01,3.48,.2))
        barrel=barrel.cut(groove)
    parts.append(record(barrel,(.028,.034,.042),'rubber'))
    parts.append(record(cyl(x,0,-.025,2.6,.12),(.035,.14,.20),'glass'))
    parts.append(record(cyl(x,0,-.04,1.5,.025),(.008,.018,.029),'glass'))
    # Small coating glint, anchored to the glass rather than to the camera view.
    parts.append(record(cyl(x-.9,-.75,-.06,.35,.02),(.24,.46,.55),'glass'))
    return parts


def sensor_board(source):
    """Detail a saved rectangular sensor envelope in its own face coordinates."""
    b=source.BoundBox
    dims=np.array([b.XLength,b.YLength,b.ZLength]);origin=np.array([b.XMin,b.YMin,b.ZMin])
    normal=int(np.argmin(dims));axes=[i for i in range(3) if i!=normal]
    r=np.column_stack([np.eye(3)[axes[0]],np.eye(3)[axes[1]],np.eye(3)[normal]])
    if np.linalg.det(r)<0:r[:,0]*=-1;origin[axes[0]]+=dims[axes[0]]
    w,h=dims[axes[0]],dims[axes[1]]
    pcb=box(0,0,0,w,h,1)
    for x in (2,w-2):
        for y in (2,h-2):pcb=pcb.cut(cyl(x,y,-.1,.75,1.2))
    parts=[record(pcb,(.035,.25,.16)),record(box(w/2-2,h/2-2,1,4,4,.7),BLACK)]
    for i in range(4):
        x=w/2-3.81+i*2.54
        parts.append(record(cyl(x,1.2,1,.65,.04),H.GOLD,'metal'))
    for x,y in ((3,h/2),(w-5,h/2),(w/2,h-3)):
        parts.append(record(box(x,y,1,1.6,.8,.5),(.56,.43,.27)))
    return [(transform(s,r,origin),c,o,t,f) for s,c,o,t,f in parts]


class Appearance:
    def __init__(self,root,open_model):
        self.wrist=open_model(root/'output/XYZ_V34_Integrated_Wrist.FCStd')
        self.camera=open_model(root.parent/'esp32_print_mount_v33/output/AITRIP_Stereo_15mm_V33.FCStd')
        self.errors={}

    def world(self,parts,source,target):
        r,t,error=register(source.Shape,target.Shape);self.errors[target.SourceKey]=error
        return [(transform(s,r,t),c,o,off,f) for s,c,o,off,f in parts]

    def parts(self,obj):
        key=obj.SourceKey
        if obj.Package=='wrist' and key.endswith('SG90_Servo_Envelope'):
            name=key.removeprefix('Wrist_');local=self.wrist.getObject(name)
            if name.startswith('Pitch'):
                r=np.array([[1,0,0],[0,0,1],[0,-1,0]]);c=np.array([0,38,-30])
            else:
                r=np.array([[0,0,1],[-1,0,0],[0,-1,0]]);c=np.array([34,0,-58])
            parts=[(transform(s,r,c),col,o,t,f) for s,col,o,t,f in servo()]
            return self.world(parts,local,obj)
        if obj.Package=='wrist' and (key.endswith('Output_Encoder') or key.endswith('Output_IMU')):
            source=self.wrist.getObject(key.removeprefix('Wrist_'))
            return self.world(sensor_board(source.Shape),source,obj)
        if obj.Package=='camera':
            name=key.removeprefix('Stereo_');source=self.camera.getObject(name)
            for prefix,z in (('Front',12.5),('Rear',33.5)):
                base=f'REF_{prefix}_'
                if name.startswith(base):
                    suffix=name[len(base):]
                    if suffix=='AITRIP_PCB':parts=camera_board(z)
                    elif suffix.startswith('Header_'):parts=camera_header((-1.43,21.43)[int(suffix[-1])],z)
                    elif suffix=='SD_Clearance':parts=sd_socket(z)
                    elif suffix=='Shield_Clearance':parts=camera_shield(z)
                    else:break
                    parts=[(optical(s),c,o,t,f) for s,c,o,t,f in parts]
                    return self.world(parts,source,obj)
            if 'Lens_Glass' in name:return []  # Included in the detailed focus barrel.
            if 'Focus_Barrel' in name:
                parts=[(optical(s),c,o,t,f) for s,c,o,t,f in lens(-7.5 if 'Left' in name else 7.5)]
                return self.world(parts,source,obj)
            color=tuple(json.loads(source.ColorRGB))
            finish='metal' if 'REF_HW_' in name else 'plastic'
            if finish=='metal':color=STEEL
            if 'Fixed_Camera_Housing' in name:color=BLACK
            return [record(obj.Shape,color,finish)]
        material=obj.Material.lower();role=obj.Role.lower();color=tuple(obj.RenderColor)[:3]
        finish='plastic'
        if 'lumber' in role or material in ('timber','plywood'):
            finish='wood';color=(1,1,1)
        elif any(s in material for s in ('steel','alumin','metal','brass','bearing','ground pin')):
            finish='metal';color=(.64,.69,.73) if 'brass' not in material else (.68,.52,.23)
        if 'Lamination_Stack' in key:finish='rubber';color=(.085,.095,.11)
        if 'Purchased_Servo_Horn' in key:color=(.86,.88,.87)
        if 'Servo_Output_Spline' in key:color=(.78,.78,.70)
        if 'Lead_Connector' in key:color=BLACK
        if 'Fixed_Camera' in key:color=BLACK
        return [record(obj.Shape,color,finish)]

    def close(self):
        App.closeDocument(self.wrist.Name);App.closeDocument(self.camera.Name)


@lru_cache(maxsize=1)
def wood_texture():
    u,v=np.meshgrid(np.linspace(0,1,512),np.linspace(0,1,512))
    phase=v*65+1.6*np.sin(u*6.28+v*8)+.5*np.sin(u*18.85+v*19)
    grain=.022*np.sin(phase)+.006*np.sin(phase*3.7)+.012*np.sin(v*35+u*2)
    grain+=np.random.default_rng(7).normal(0,.002,grain.shape)
    pixels=np.clip(np.array([.68,.50,.32])+grain[:,:,None],0,1)
    pixels=(pixels*255).astype(np.uint8)
    image=vtk.vtkImageData();image.SetDimensions(512,512,1)
    image.GetPointData().SetScalars(numpy_to_vtk(pixels.reshape(-1,3),deep=True))
    texture=vtk.vtkTexture();texture.SetInputData(image);texture.InterpolateOn();texture.RepeatOn()
    return texture


def wood_mesh(vertices,faces):
    """Map grain along each timber's longest dimension, across each side face."""
    xyz=np.array([[p.x,p.y,p.z] for p in vertices]);grain_axis=int(np.argmax(np.ptp(xyz,axis=0)))
    points=vtk.vtkPoints();cells=vtk.vtkCellArray();uv=vtk.vtkFloatArray();uv.SetNumberOfComponents(2)
    for face in faces:
        tri=xyz[list(face)];normal=np.cross(tri[1]-tri[0],tri[2]-tri[0]);face_axis=int(np.argmax(abs(normal)))
        other=[i for i in range(3) if i not in (grain_axis,face_axis)]
        across=other[0];along=grain_axis if face_axis!=grain_axis else other[-1]
        cells.InsertNextCell(3)
        for p in tri:
            cells.InsertCellPoint(points.InsertNextPoint(*p))
            uv.InsertNextTuple2(p[along]/120,p[across]/45)
    mesh=vtk.vtkPolyData();mesh.SetPoints(points);mesh.SetPolys(cells);mesh.GetPointData().SetTCoords(uv)
    return mesh
