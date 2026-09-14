"""Product-reference geometry for portfolio illustrations, not manufacturing CAD.

Layouts follow the selected Amazon product photographs in papaw-hardware-audit.md.
Small packages and optical details are visual approximations. Coordinates use X/Z
for the board face and +Y for the component side. No source enclosure is modified.
"""
from collections import defaultdict
from functools import lru_cache
import math

import FreeCAD as App
import Part

V = App.Vector
BLACK = (.035, .042, .050)
SILVER = (.68, .72, .76)
GOLD = (.79, .63, .30)
WHITE = (.84, .87, .89)
BLUE = (.045, .18, .40)
GREEN = (.035, .29, .19)
CERAMIC = (.60, .47, .31)


def box(x, y, z, w, d, h):
    return Part.makeBox(w, d, h, V(x, y, z))


def cylinder(x, y, z, r, depth):
    return Part.makeCylinder(r, depth, V(x, y, z), V(0, 1, 0))


def rounded(x, y, z, w, d, h, radius):
    s = box(x, y, z, w, d, h)
    edges = [e for e in s.Edges if abs(e.BoundBox.YLength - d) < 1e-6
             and e.BoundBox.XLength < 1e-6 and e.BoundBox.ZLength < 1e-6]
    return s.makeFillet(radius, edges)


def add(parts, shape, color, opacity=1):
    parts.append((shape, color, opacity, None))


def grouped(parts):
    groups = defaultdict(list)
    for shape, color, opacity, _ in parts:
        groups[(color, opacity)].append(shape)
    return [(Part.makeCompound(shapes), color, opacity, None)
            for (color, opacity), shapes in groups.items()]


def placed(parts, x, y, z, quarter_turn=False):
    result = []
    for shape, color, opacity, _ in parts:
        s = shape.copy()
        if quarter_turn:
            # USB at the top of the tall PIR enclosure.
            s.rotate(V(0, 0, 0), V(0, 1, 0), 90)
            s.translate(V(0, 0, 22.5))
        s.translate(V(x, y, z))
        result.append((s, color, opacity, None))
    return result


@lru_cache(maxsize=80)
def lettering(text, height):
    chars = Part.makeWireString(text, 'C:/Windows/Fonts/', 'arial.ttf', height)
    faces = [Part.makeFace(wires, 'Part::FaceMakerBullseye') for wires in chars if wires]
    s = Part.makeCompound(faces).extrude(V(0, 0, .025))
    s.rotate(V(0, 0, 0), V(1, 0, 0), 90)
    s.rotate(V(0, 0, 0), V(0, 0, 1), 180)
    return s


def label(parts, text, x, y, z, height=1, color=WHITE):
    s = lettering(text, height).copy()
    b = s.BoundBox
    s.translate(V(x - (b.XMin + b.XMax) / 2, y - b.YMin, z - b.ZMin))
    add(parts, s, color)


def smd(parts, x, y, z, w=1.6, h=.8, d=.45, color=CERAMIC):
    add(parts, box(x, y, z, w, d, h), color)
    ends = [box(x-.04, y-.03, z, w*.2, d+.06, h),
            box(x+w*.8, y-.03, z, w*.2+.04, d+.06, h)]
    add(parts, Part.makeCompound(ends), SILVER)


def chip(parts, x, y, z, w, h, d, pins=8, diagonal=False):
    body = box(x, y, z, w, d, h)
    leads = []
    for i in range(pins):
        px = x + .35 + i * (w-.7)/(pins-1)
        pz = z + .35 + i * (h-.7)/(pins-1)
        leads.extend([box(px-.09, y, z-.22, .18, .18, .36),
                      box(px-.09, y, z+h-.14, .18, .18, .36),
                      box(x-.22, y, pz-.09, .36, .18, .18),
                      box(x+w-.14, y, pz-.09, .36, .18, .18)])
    leads = Part.makeCompound(leads)
    if diagonal:
        for s in (body, leads):
            s.rotate(V(x+w/2, y, z+h/2), V(0, 1, 0), 45)
    add(parts, body, BLACK)
    add(parts, leads, SILVER)


@lru_cache(maxsize=1)
def esp32():
    parts = []
    pcb = rounded(0, 0, 0, 22.5, 1, 18, .45)
    pads = []
    for i in range(8):
        x = 1.65 + i * 2.54
        for z, edge in ((1.2, 0), (16.8, 18)):
            bore = cylinder(x, -.1, z, .48, 1.3)
            scallop = cylinder(x, -.1, edge, .36, 1.3)
            pcb = pcb.cut(bore).cut(scallop)
            for y in (-.025, 1):
                pads.append(cylinder(x, y, z, .88, .025).cut(bore))
    add(parts, pcb, BLACK)
    add(parts, Part.makeCompound(pads), GOLD)
    # Formed metal USB-C shell, open mouth, tongue, and contacts.
    usb = rounded(-1.9, 1, 4.5, 6.4, 3.2, 9, .6)
    mouth = rounded(-2.05, 1.3, 4.8, 4.8, 2.6, 8.4, .45)
    add(parts, usb.cut(mouth), SILVER)
    add(parts, box(-1.55, 2.40, 5.35, 3.7, .55, 7.3), BLACK)
    contacts = [box(-1.4, 2.96, 5.8+i*.5, 1.8, .035, .19) for i in range(12)]
    add(parts, Part.makeCompound(contacts), GOLD)
    for z in (3.85, 13.2):
        add(parts, box(1.5, 1, z, 2.5, .22, .9), SILVER)
    for z in (4.0, 11.0):
        add(parts, rounded(5.4, 1, z, 3.6, 1.05, 3.9, .25), BLACK)
        add(parts, box(5.6, 2.05, z+.15, 3.2, .16, 3.6), SILVER)
        add(parts, cylinder(7.2, 2.21, z+1.95, 1.12, .35), BLACK)
        for x in (5.15, 8.75):
            add(parts, box(x, 1.05, z+.6, .5, .25, 2.7), SILVER)
    chip(parts, 10.65, 1, 6.15, 5, 5, .95, diagonal=True)
    add(parts, rounded(16.75, 1, 2.2, 3.1, .8, 2.55, .25), SILVER)
    label(parts, '40', 18.3, 1.81, 2.85, .65, BLACK)
    smd(parts, 20.5, 1, 6.8, 1.6, 4.8, 1.1, (.61, .035, .025))
    label(parts, 'C3', 21.3, 2.12, 8.45, .9)
    smd(parts, 11.0, 1, 2.1, 2.6, 1.6, 1.0, BLACK)
    for x, z in ((9.7,3.1),(14.2,2.2),(15.0,4.6),(9.5,13.0),(12.2,14.4),
                 (16.9,13.8),(19.5,12.6),(17.4,6.2),(18.4,11.6)):
        smd(parts, x, 1, z, 1.15, .65, .35)
    for z, color in ((14.0,(.52,.04,.04)),(12.5,(.06,.18,.62))):
        smd(parts, 3.8, 1, z, 1.2, .7, .45, color)
    label(parts, 'ESP32-C3', 13.2, 2, 8.0, .63)
    label(parts, 'BOOT', 7.1, 1.02, 2.3, .7)
    label(parts, 'RST', 7.1, 1.02, 15.1, .7)
    for i, text in enumerate(('5V','G','3V3','4','3','2','1','0')):
        label(parts, text, 1.65+i*2.54, 1.02, 14.7, .55)
    return grouped(parts)


@lru_cache(maxsize=1)
def regulator():
    parts = []
    pcb = box(0, 0, 0, 30, 1.6, 16)
    for x in (1.4, 28.6):
        for z in (1.5, 3.3, 12.7, 14.5):
            bore = cylinder(x, -.1, z, .43, 1.9)
            pcb = pcb.cut(bore)
            add(parts, cylinder(x, 1.6, z, .8, .03).cut(bore), SILVER)
    add(parts, pcb, BLUE)
    # Shielded 1R5 inductor, tantalum capacitor, QFN and ceramic network.
    add(parts, rounded(11.5, 1.6, 7.4, 7, 3.8, 7, .55), (.25,.27,.29))
    add(parts, box(10.9, 1.65, 9, 8.2, .4, 3.8), SILVER)
    label(parts, '1R5', 15, 5.42, 9.7, 1.6, (.12,.14,.15))
    chip(parts, 12.1, 1.6, 2.9, 3.3, 3.3, .8, pins=5)
    smd(parts, 4.4, 1.6, 3.2, 4.1, 3.7, 2.1, (.79,.36,.09))
    add(parts, box(4.5, 3.72, 3.5, .3, .025, 3.1), (.38,.13,.035))
    for x, z in ((8.9,4.0),(19.6,7.4),(22,7.4),(24.4,7.4),
                 (18.4,3),(20.8,3),(23.2,3),(10.3,2.7)):
        smd(parts,x,1.6,z,1.7,1.0,.65)
    for i, text in enumerate(('EN','PS','ADJ','5V','3V3')):
        x = 5 + i*4.7
        for px in (x-.45, x+.1):
            add(parts, box(px,1.6,.25,.35,.04,.7), SILVER)
        label(parts,text,x,1.64,1.05,.68)
    for text,x,z in (('VIN',3.7,12.1),('GND',3.7,.7),('OUT',26,12.1)):
        label(parts,text,x,1.64,z,.82)
    return grouped(parts)


def fresnel(parts):
    # Geodesic cells reproduce the recognizable faceted surface of the product.
    phi=(1+math.sqrt(5))/2
    verts=[V(-1,phi,0),V(1,phi,0),V(-1,-phi,0),V(1,-phi,0),
           V(0,-1,phi),V(0,1,phi),V(0,-1,-phi),V(0,1,-phi),
           V(phi,0,-1),V(phi,0,1),V(-phi,0,-1),V(-phi,0,1)]
    verts=[v/v.Length for v in verts]
    faces=[(0,11,5),(0,5,1),(0,1,7),(0,7,10),(0,10,11),(1,5,9),
           (5,11,4),(11,10,2),(10,7,6),(7,1,8),(3,9,4),(3,4,2),
           (3,2,6),(3,6,8),(3,8,9),(4,9,5),(2,4,11),(6,2,10),
           (8,6,7),(9,8,1)]
    cache={}
    def midpoint(a,b):
        key=tuple(sorted((a,b)))
        if key not in cache:
            v=verts[a]+verts[b];cache[key]=len(verts);verts.append(v/v.Length)
        return cache[key]
    refined=[]
    for a,b,c in faces:
        ab,bc,ca=midpoint(a,b),midpoint(b,c),midpoint(c,a)
        refined.extend(((a,ab,ca),(b,bc,ab),(c,ca,bc),(ab,bc,ca)))
    centers=[]
    neighbors=defaultdict(list)
    for tri in refined:
        v=sum((verts[i] for i in tri),V());v=v/v.Length
        for i in tri:neighbors[i].append(v)
    center=V(16,9,12)
    cap=Part.makeSphere(11.25,center).common(box(3,9,-1,26,13,26))
    add(parts,cap,(.85,.89,.91))
    for i,normal in enumerate(verts):
        if normal.y < -.2:continue
        tangent=normal.cross(V(0,1,0))
        if tangent.Length < .01:tangent=normal.cross(V(1,0,0))
        tangent=tangent/tangent.Length;other=normal.cross(tangent)
        points=sorted(neighbors[i],key=lambda v:math.atan2(v.dot(other),v.dot(tangent)))
        polygon=[]
        for v in points:
            delta=(v-normal*v.dot(normal))*11.5*.99
            polygon.append(center+normal*11.35+delta)
        # Clip the equatorial polygons to the mounting plane.
        clipped=[]
        for a,b in zip(polygon,polygon[1:]+polygon[:1]):
            if a.y >= 9:clipped.append(a)
            if (a.y>=9)!=(b.y>=9):clipped.append(a+(b-a)*((9-a.y)/(b.y-a.y)))
        if len(clipped)<3:continue
        face=Part.Face(Part.makePolygon(clipped+[clipped[0]]))
        add(parts,face.extrude(normal*.10),(.90,.93,.94))


@lru_cache(maxsize=1)
def pir():
    parts=[]
    pcb=box(0,0,0,32,1.6,24)
    for x in (1.65,30.35):
        bore=cylinder(x,-.1,12,1.4,1.9);pcb=pcb.cut(bore)
    add(parts,pcb,GREEN)
    add(parts,rounded(4.0,8.1,.0,24,.9,24,.8),(.87,.90,.91))
    fresnel(parts)
    # Backside trimmers and electrolytic capacitors remain visible while rotating.
    for x,z in ((2.8,2.8),(29.2,2.8),(3.0,21.2),(29.0,21.2)):
        add(parts,cylinder(x,-6.7,z,2.3,6.7),BLACK)
        add(parts,cylinder(x,-6.76,z,2.15,.08),SILVER)
    for x in (9,23):
        pot=cylinder(x,-5.1,3.4,2.7,5.1)
        slot=box(x-.3,-5.2,1.6,.6,1,3.6)
        add(parts,pot.cut(slot),(.70,.32,.07))
    chip(parts,11.7,-1.5,9.8,8.2,4,1.5,pins=8)
    for x,z in ((4,7),(8,16),(14,16),(20,16),(26,7),(9,20),(17,20),(23,20)):
        smd(parts,x,-.7,z,2,1,.7)
    add(parts,box(29,-2.5,16,2.4,2.5,7.5),BLACK)
    for z in (17,19.54,22.08):
        add(parts,box(29.85,-8,z,.64,8.2,.64),GOLD)
    for x in (2.7,29.3):
        for z in (5.2,8,16,18.8):
            add(parts,cylinder(x,1.6,z,.65,.24),SILVER)
    label(parts,'HC-SR501',16,1.64,23.0,.68)
    return grouped(parts)


@lru_cache(maxsize=1)
def oled():
    parts=[]
    pcb=box(0,0,0,27.6,1.2,27.6)
    for x in (2.05,25.55):
        for z in (2.05,25.55):
            bore=cylinder(x,-.1,z,1.25,1.5);pcb=pcb.cut(bore)
            add(parts,cylinder(x,1.2,z,1.8,.03).cut(bore),SILVER)
    add(parts,pcb,BLUE)
    add(parts,box(1.2,1.2,6.5,25.2,1.55,14.6),(.025,.035,.052))
    add(parts,box(2.95,2.76,8.35,21.7,.04,10.9),(.04,.085,.115))
    # Flex ribbon and separate four-pin connector, with the header facing the ESP.
    add(parts,box(5.8,1.25,21.1,16,.18,3.3),(.48,.25,.07))
    traces=[box(6.1+i*.48,1.44,21.15,.12,.02,2.9) for i in range(32)]
    add(parts,Part.makeCompound(traces),GOLD)
    add(parts,box(8.72,-2.5,.3,10.16,2.5,2.5),BLACK)
    for i in range(4):
        x=10+i*2.54
        add(parts,box(x-.32,-6,.95,.64,7.5,.64),GOLD)
        add(parts,cylinder(x,1.2,1.27,.8,.15),SILVER)
    label(parts,'SDA SCL GND VCC',13.8,1.22,3.4,.83)
    for x,z in ((3.5,6),(7.5,6),(12,6),(17,6),(21,6),(6,23),(18,23)):
        smd(parts,x,-.65,z,1.8,1,.65)
    return grouped(parts)


def reed(x,y,z):
    parts=[]
    glass=Part.makeCylinder(1.14,14,V(x,y,z),V(0,0,1))
    add(parts,glass,(.34,.63,.51),.38)
    for start in (z-4,z+14):
        add(parts,Part.makeCylinder(.27,4,V(x,y,start),V(0,0,1)),SILVER)
    add(parts,box(x-.45,y-.12,z,.9,.24,7.2),SILVER)
    add(parts,box(x-.45,y+.20,z+6.8,.9,.24,7.2),SILVER)
    return grouped(parts)


def battery_details(x):
    parts=[]
    for i,z in enumerate((8,19.5,31)):
        for end in (x,x+42.8):
            add(parts,Part.makeCylinder(5.24,1.7,V(end,8,z),V(1,0,0)),SILVER)
        positive=x+.1 if i==1 else x+44.15
        add(parts,Part.makeCylinder(1.8,.25,V(positive,8,z),V(1,0,0)),SILVER)
        label(parts,'AAA',x+20,13.27,z-.85,1.65)
        label(parts,'+',x+5 if i==1 else x+39,13.27,z-.7,1.4)
    return grouped(parts)
