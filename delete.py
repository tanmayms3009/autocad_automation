#Using comtype modules:
import win32com.client

acad = win32com.client.Dispatch("AutoCAD.Application")
acadModel = acad.ActiveDocument.ModelSpace #Works same as acad.model  
for object in acadModel:
    if object.ObjectName == "AcDbCircle":
        object.Delete()


#############################################

#Using pyautocad module:

# from pyautocad import Autocad

# acad = Autocad(create_if_not_exists=True)


# for object in acad.iter_objects("AcDbCircle"):
#     object.Delete()