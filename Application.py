from pyautocad import Autocad, APoint, aDouble
import time

acad = Autocad(create_if_not_exists=True)

#Application details
print(acad.app.Application.Name)
print(acad.app.Caption)
print(acad.app.ActiveDocument.Name)

#Get the window handle of the window frame.
print(acad.app.Path)
print(acad.app.FullName)


print(acad.app.Documents)
for i in acad.app.Documents:
    print(i.Name)

#Get local id of current autocad session
print(acad.app.LocaleId)

#Get menu bar object from the session
print(acad.app.MenuBar)

#A collection of PopupMenu objects representing the current AutoCAD menu bar.
print(acad.app.MenuGroups)
for i in acad.app.MenuGroups:
    print(i.Name)


print(acad.app.HWND)


#Application Dimensions
print(acad.app.Height)
print(acad.app.Width)

#Get current active status of viewport
print(acad.app.StatusID)

#Specify if window is minimized, mzximized or normal
print(acad.app.WindowState)

#
print(acad.app.WindowTop)
print(acad.app.WindowLeft)

#Test if autocad is in a quiescent state or not
print(acad.app.GetAcadState().IsQuiescent)

#Close drawing file and exist application
acad.app.Quit()

#Update the application
acad.app.Update()


##################################################3
from win32com.client import *
import pythoncom
import win32com

acad1 = win32com.client.Dispatch("AutoCAD.Application")

print(acad1.Application.Name)