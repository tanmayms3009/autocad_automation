from pydoc import Doc
import time
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


#Circle
c1 = acad.AddCircle(ap(100, 100, 0), 50)
c2 = acad.AddCircle(ap(100, 100, 0), 45)

###################################################################################################################

r1 = acad.AddRegion(win32com.client.VARIANT(VT_ARRAY | VT_DISPATCH, (c1, c2)))

a1 = acad.AddLine(ap(1000, 1000, 0), ap(1000, 1000, 1500))


for obj in acad:
    if obj.ObjectName=="AcDbRegion":
        print(obj.ObjectName)
        time.sleep(5)
        acad.AddExtrudedSolidAlongPath(obj, a1)
        break    

