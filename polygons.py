from array import array
#os.X_OK: Checks if path can be executed.
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
#Converting list to tuple as pyautocad accepts tuple as input
ccct = tuple(ccc)
print('The coordinates for the center of circle : ',ccct)
#Radius
rc = float(input("Enter the radius of Circle: "))

#3. Calculate coordinates
i=0
#Creating an empty list for coordinates
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
#Converting list to tuple as pyautocad accepts tuple as input
pgont=tuple(pgonc)
print("Coordinates of Polygon: ")
print(pgont)

#4.Draw Polygon
#To specify coordinates of a polygon we need to use aDuble method:
polygon = aDouble(pgont)
#To draw polygon we need to use AddPolyline method:
polygond = acad.model.AddPolyline(polygon)
#Rotate the Polygon
polygond1 = polygond.Rotate(APoint(100, 25, 0), 3.14*185/180)

#Other Utilities:
pa = polygond.Area
print("Perimeter of Polygon: " + str(pa))
pl = polygond.Length
print("Perimeter of Polygon: " + str(pl))
is_closed = polygond.Closed
print("Is the Polyline Object a Closed space: " + str(is_closed))
#We can specify coordinates of a single vertex by passing vertex index no as a parameter to Coordinate method:
print("Elevation of Vertex: ")
print(polygond.Coordinate(1))
#We can get coordinates of all the vertices of Polygon with Coordinates method:
print("Elevation of Polyline: ")
print(polygond.Coordinates)
print("Elevation of Polyline: " + str(polygond.Elevation))
print("Perimeter of Polygon: " + polygond.Layer)


