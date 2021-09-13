from array import array
from os import X_OK
from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

#1. Type the number of angles n-gone is supposed to have:
na = int(input("Enter the number of angles / vertices for the n-gone: "))

#2. Center & Radius of Circle
#Center
cc = input("Enter x, y coordinates for center of circle with comma separators e.g. x, y: ")
ccc = (map(float, cc.split(", ")))
ccct = tuple(ccc)
print('The coordinates for the center of circle : ',ccct)
#Radius
rc = float(input("Enter the radius of Circle: "))

#3. Calculate coordinates
i=0
pgonc=[]
for i in range(na):
    x=round(ccct[0]+rc*cos(2*pi*i/na),2)
    y=round(ccct[1]+rc*sin(2*pi*i/na),2)
    z=0
    crd = [x, y, z]
    pgonc.extend(crd)
    i += 1
#Addind first point again to complete the loop of polygon
fp = [pgonc[0], pgonc[1], pgonc[2]]
pgonc.extend(fp)
print(pgonc)
#Converting list to tuple as pyautocad accepts tuple as input
pgont=tuple(pgonc)


#4.Draw Polygon
#To specify coordinates of a polygon we need to use aDuble method:
polygon = aDouble(pgont)
#To draw polygon we need to use AddPolyline method:
acad.model.AddPolyline(polygon)
