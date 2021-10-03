from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

#Rectangular array

def array_rectangle(x, y, z, r, c, lr, dr, dc, dl):
    l=int(input("Enter length of rectangle:"))
    b=int(input("Enter breadth of rectangle:"))
    rect = (x, y, z, x, y+b, z, x+l, y+b, z, x+l, y, z, x, y, z)
    rec = acad.model.AddPolyline(aDouble(rect))
    arr1 = rec.ArrayRectangular(r, c, lr, dr+b, dc+l, dl)
array_rectangle(50, 150, 0, 3, 3, 1, 150, 250, 0)


def array_circle(x, y, rad,  r, c, lr, dr, dc, dl):
    c1 = acad.model.AddCircle(APoint(x, y), rad)
    arr2 = c1.ArrayRectangular(r, c, lr, dr+rad*2, dc+rad*2, dl)    
array_circle(100, 100, 100, 3, 3, 1, 50, 100, 0)

