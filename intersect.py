from pyautocad import Autocad, APoint, aDouble
from math import pi

acad = Autocad(create_if_not_exists=True)

#acExtendNone
# c1 = acad.model.AddCircle(APoint(100, 100, 0), 75)
# c2 = acad.model.AddCircle(APoint(100, 200, 0), 75)
# print(c1.IntersectWith(c2, 0))

#acExtendThisEntity
# a1 = acad.model.AddArc(APoint(150, 105, 0), 75, 0, round(105*pi/180,2))
# l1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
# print(l1.IntersectWith(a1, 1))
# print(l1.IntersectWith(a1, 2))

#acExtendBoth
l1 = acad.model.AddLine(APoint(0, 0, 0), APoint(100, 100, 0))
l2 = acad.model.AddLine(APoint(300, 0, 0), APoint(200, 100, 0))
print(l1.IntersectWith(l2, 1))
