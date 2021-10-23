import win32com.client
import pythoncom
from math import pi

acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace

def APoint(x, y, z = 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

def ADouble(xyz):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (xyz))

def variants(object):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, (object))


out_loop = []
sq = acadModel.AddPolyline(ADouble([0,0,0,1000,0,0,1000,1000,0,0,1000,0]))
arc = acadModel.AddArc(APoint(0, 500, 0), 500, 90*pi/180, 270*pi/180)
out_loop.append(sq)
out_loop.append(arc)

outer = variants(out_loop)

hatch = acadModel.AddHatch(0, "ANSI37", True,)
hatch.AppendOuterLoop(outer)


print(hatch.HatchStyle)
print(hatch.PatternName)
print(hatch.AssociativeHatch)

print(round(hatch.Area,2))
print(hatch.PatternAngle)
print(hatch.PatternDouble)
print(hatch.PatternScale)
print(hatch.PatternSpace)
print(hatch.PatternType)
print(hatch.NumberOfLoops)

hatch.PatternScale = 10

in_loop = []
in_loop.append(acadModel.AddCircle(APoint(250, 250, 0), 100))
inner = variants(in_loop)
hatch.AppendInnerLoop(inner)
print(round(hatch.Area,2))