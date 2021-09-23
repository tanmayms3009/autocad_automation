from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

#Arc
p1 = APoint(30,30)
#autocad.model.AddCircle(<Center Point of Circle>, <Radius>, <Initial Angle>, <Final Angle>)
#Command uses angle in Radians and not in Degrees (We can convert to degrees using math module):
#Arc is draws COUNTERCLOCKWISE
arc1 = acad.model.AddArc(p1, 7.5, 0, 4)
arc2 = acad.model.AddArc(APoint(45, 45), 10, 15*pi/180 , 105*pi/180)


#Properties:

#Area of Arc:
a1a = print("Area of Arc1 = " + str(round(arc1.Area,2)))
a2a = print("Area of Arc2 = " + str(round(arc2.Area,2)))

#Other Properties:

#Center of Arc
a1c = print("Center of Arc1 = " + str(arc1.Center))
a2c = print("Center of Arc2 = " + str(arc2.Center))

#Radius of Arc
a1c = print("Radius of Arc1 = " + str(arc1.Radius))
a2c = print("Radius of Arc2 = " + str(arc2.Radius))

#Start & End points of Arc
a1sp = print("Start point of Arc1 = " + str(arc1.StartPoint))
a1ep = print("End point of Arc1 = " + str(arc1.EndPoint))
a2sp = print("Start point of Arc2 = " + str(arc2.StartPoint))
a2ep = print("End point of Arc2 = " + str(arc2.EndPoint))

#Start & End angles of Arc
a1sa = print("Start angle of Arc1 = " + str(arc1.StartAngle))
a1ea = print("End angle of Arc1 = " + str(arc1.EndAngle))
a2sa = print("Start angle of Arc2 = " + str(arc2.StartAngle))
a2ea = print("End angle of Arc2 = " + str(arc2.EndAngle))
