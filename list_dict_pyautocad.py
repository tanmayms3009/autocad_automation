from pyautocad import Autocad, APoint, aDouble

acad = Autocad()

line1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
line2 = acad.model.AddLine(APoint(200, 0, 0), APoint(100, 100, 0))

circle1 = acad.model.AddCircle(APoint(100, 250, 0), 50)
pl1 = acad.model.AddPolyline(aDouble(0, 0, 0, 100, 0, 0, 100, 100, 0, 0, 100, 0, 0, 0, 0))

ls_line = []
ls_line.append(line1)
ls_line.append(line2)

ls_mixed = []
ls_mixed.append(circle1)
ls_mixed.append(pl1)
dict_mixed = {"round": circle1, "square": pl1}


for l in ls_line:
    l.ScaleEntity(APoint(l.StartPoint), 2)

# for j in dict:
#     if j.ObjectName == "AcDbCircle":
#         j.ScaleEntity(APoint(j.Center), 2)
#     elif j.ObjectName == "AcDb2dPolyline":
#         j.ScaleEntity(APoint(j.Coordinate(4)), 4)

for j in dict_mixed:
     if j == "round":
         dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Center), 2)
     if j == "round":
         dict_mixed[j].ScaleEntity(APoint(dict_mixed[j].Center), 2)
