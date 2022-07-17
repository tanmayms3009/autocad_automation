from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

ip = APoint(0, 0, 0)
b1 = acad.doc.Blocks.Add(ip, "Attributed_Block_1")

pl = b1.AddPolyline(aDouble(0, 0, 0, 10000, 0, 0, 10000, 5000, 0, 0, 5000, 0, 0, 0, 0))
l = b1.AddLine(APoint(0, 250, 0), APoint(10000, 250, 0))
l = b1.AddLine(APoint(5000, 250, 0), APoint(5000, 0, 0))

#0, 1, 2, 3, 4, 5, 6 .... 10
a1 = b1.AddAttribute(50, 0, "DATE", aDouble(200, 100, 0), "DATE", "Date: 17/07/2022")
a2 = b1.AddAttribute(50, 0, "DWG", aDouble(5200, 100, 0), "DWG", "Drawing Name: Drawing 1")

br = acad.model.InsertBlock(APoint(50, 50, 0), "Attributed_Block_1", 1, 1, 1, 0)

print("Does the Block contain any Attributes: ", end="")
print(br.HasAttributes)