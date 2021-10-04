from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

#Polar array

#object.ArrayPolar(NumberOfObjects, AngleToFill, CenterPoint)

c1 = acad.model.AddCircle(APoint(100, 100), 100)
arr1 = c1.ArrayPolar(10, round(pi*180/180), aDouble(550, 600, 0))
