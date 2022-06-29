from pydoc import Doc
import win32com.client
from pythoncom import VT_ARRAY, VT_R8, VT_DISPATCH
from pyautocad import Autocad, APoint

###################################################################################################################

def ap(x, y, z = 0):
    return win32com.client.VARIANT(VT_ARRAY | VT_R8, (x, y, z))

def ad(*argv):
    return win32com.client.VARIANT(VT_ARRAY | VT_R8, (argv))

###################################################################################################################

app = win32com.client.Dispatch("AutoCAD.Application")
doc = app.ActiveDocument
acad = doc.ModelSpace

###################################################################################################################

#Enclosed polyline
pl1 = acad.AddPolyline(ad(0,0,0,1000,0,0,1000,500,0,750,500,0,750,1000,0,250,1000,0,250,500,0,0,500,0,0,0,0))

#Circle
c1 = acad.AddCircle(ap(500, 1000, 0), 250)

###################################################################################################################

acad.AddRegion(win32com.client.VARIANT(VT_ARRAY | VT_DISPATCH, (pl1, c1)))

###################################################################################################################

acad1 = Autocad(create_if_not_exists=True)

regions = {}
i=0
for l in acad1.iter_objects_fast(object_name_or_list="Region"):
    print(str(l.ObjectID) + ": " + l.ObjectName)
    key = "reg" + str(i)
    regions[key] = l
    i+=1

regions["reg1"].Boolean(2, regions["reg0"])

for l in acad1.iter_objects_fast(object_name_or_list="Region"):
    print(str(l.ObjectID) + ": " + l.ObjectName)
    l.Move(APoint(0, 0, 0), APoint(1500, 0, 0))
