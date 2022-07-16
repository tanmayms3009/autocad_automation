from pyautocad import Autocad, APoint, aDouble
import time

acad = Autocad(create_if_not_exists=True)


print(acad.doc.Name)

#Determine if the document is the active document
print(acad.doc.Active)

#Different Active properties
print(acad.doc.ActiveDimStyle.Name)
print(acad.doc.ActiveLayer.Name)
print(acad.doc.ActiveLayout.Name)


#Get the blocks collection from the drawing
print(acad.doc.Blocks)
for i in (acad.doc.Blocks):
    print(i.Name)

#Get the database in which the object belongs
print(acad.doc.Database)


print(acad.doc.DimStyles)
for i in (acad.doc.DimStyles):
    print(i.Name)

print(acad.doc.ElevationModelSpace)
print(acad.doc.ElevationPaperSpace)


print(acad.doc.Height)
print(acad.doc.Width)
print(acad.doc.Limits)
print(acad.doc.ObjectSnapMode)
print(acad.doc.Path)
print(acad.doc.ReadOnly)
print(acad.doc.Saved)
print(acad.doc.SummaryInfo)
print(acad.doc.WindowState)
print(acad.doc.WindowTitle)


acad.doc.Active
acad.doc.AuditInfo(True)

acad.doc.Regen
acad.doc.Save
#acad.doc.Close(False, "Drawing2.dwg")
acad.doc.PurgeAll