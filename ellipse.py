from pyautocad import Autocad, APoint
from math import *

acad = Autocad(create_if_not_exists=True)

#Ellipse
p1 = APoint(35, 35)
p2 = APoint(40, 35)
#el1 = autocad.model.AddEllipse(<Centre of Ellipse>, <Greater radius size>, <Ratio of greater to smaller radius>)
el1 = acad.model.AddEllipse(p1, p2, 0.5)
#The ellipse is formed on the basis of the second argument we provide here:p2
#The greater radius is created on the basis of second argument in the direction of vector that is formed due to the points we passed in the same
#e.g. If p1 = (0, 0) & p2 = (1, 1) ; Hypotanius of x = 1, y = 1 is 1.41. Hence Graeter Radius  = 1.41

el2 = acad.model.AddEllipse(APoint(100, 50), APoint(150, 50), 0.5)
el2.StartAngle = round(45 * (3.14 / 180),2)
el2.EndAngle = round(270 * (3.14 / 180),2)

print("Ellipse 1 properties: " + "\n" +
"Area of Ellipse 1 = " + str(round(el1.Area,2)) + "\n" +
"Center of Ellipse 1 = " + str(el1.Center) + "\n" +
"Start point of Ellipse 1 = " + str(el1.StartPoint) + "\n" +
"End point of Ellipse 1 = " + str(el1.EndPoint) + "\n" +
"Start angle of Ellipse 1 = " + str(round(el1.StartAngle,2)) + "\n" +
"End angle of Ellipse 1 = " + str(round(el1.EndAngle,2)) + "\n" +
"Start parameter of Ellipse 1 = " + str(el1.StartParameter) + "\n" +
"End parameter of Ellipse 1 = " + str(el1.EndParameter) + "\n" +
"Major axis of Ellipse 1 = " + str(el1.MajorAxis) + "\n" +
"Minor axis of Ellipse 1 = " + str(el1.MinorAxis) + "\n" +
"Major radius of Ellipse 1 = " + str(round(el1.MajorRadius,2)) + "\n" +
"Minor radius of Ellipse 1 = " + str(round(el1.MinorRadius,2)) + "\n" + 
"Radius ratio of Ellipse 1 = " + str(el1.RadiusRatio)
)

print("Ellipse 2 properties: " + "\n" +
"Area of Ellipse 2 = " + str(round(el2.Area,2)) + "\n" +
"Center of Ellipse 2 = " + str(el2.Center) + "\n" +
"Start point of Ellipse 2 = " + str(el2.StartPoint) + "\n" +
"End point of Ellipse 2 = " + str(el2.EndPoint) + "\n" +
"Start angle of Ellipse 2 = " + str(round(el2.StartAngle,2)) + "\n" +
"End angle of Ellipse 2 = " + str(round(el2.EndAngle,2)) + "\n" +
"Start parameter of Ellipse 2 = " + str(el2.StartParameter) + "\n" +
"End parameter of Ellipse 2 = " + str(el2.EndParameter) + "\n" +
"Major axis of Ellipse 2 = " + str(el2.MajorAxis) + "\n" +
"Minor axis of Ellipse 2 = " + str(el2.MinorAxis) + "\n" +
"Major radius of Ellipse 2 = " + str(round(el2.MajorRadius,2)) + "\n" +
"Minor radius of Ellipse 2 = " + str(round(el2.MinorRadius,2)) + "\n" + 
"Radius ratio of Ellipse 2 = " + str(el2.RadiusRatio)
 )

acad.app.ZoomExtents()