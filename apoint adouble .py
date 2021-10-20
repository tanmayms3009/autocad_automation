from win32com.client import *
import pythoncom

acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace #Works same as acad.model  

def APoint(x, y, z = 0):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (x, y, z))

def ADouble(*argv):
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, (argv))



########################################################################################
