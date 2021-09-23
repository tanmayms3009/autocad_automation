from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

#(Origin/Center, Length, Width, Height)
box = acad.model.AddBox(APoint(0, 0, 0), 1000, 1200, 750)
#(Center, Base radius, Height)
cone = acad.model.AddCone(APoint(2000, 0, 0), 750, 800)
#(Center, Radius, Height)
cyl =  acad.model.AddCylinder(APoint(3200, 0, 0), 350, 1250)
#(Center, MajorRadius, MinorRadius, Height)
econe =  acad.model.AddEllipticalCone(APoint(4000, 500 , 0), 450, 225, 1275.62)
#(Center, MajorRadius, MinorRadius, Height)
ecyl =  acad.model.AddEllipticalCylinder(APoint(1500, 2000 , 0), 750, 400, 950)
#(Center, Radius)
sph = acad.model.AddSphere(APoint(2500, 3500, 0), 250)
#(Center, TorusRadius, TubeRadius)
tor = acad.model.AddTorus(APoint(1000, 4000, 0), 500, 100)
#(Center, Length, Width, Height)
wed = acad.model.AddWedge(APoint(2000, 5000, 0), 1000, 1200, 750)
 

print("Volume of box: " + str(box.Volume))
print("Centroid of box: " + str(box.Centroid))
print("Moment of Inertia of box: " + str(box.MomentOfInertia))
print("Product of inertia of box: " + str(box.ProductOfInertia))
print("Principal directions of box: " + str(box.PrincipalDirections))
print("Principal moments of box: " + str(box.PrincipalMoments))
print("Radius of giration of box: " + str(box.RadiiOfGyration))


print("Volume of Torus: " + str(tor.Volume))
print("Centroid of Torus: " + str(tor.Centroid))
print("Moment of Inertia of Torus: " + str(tor.MomentOfInertia))
print("Product of inertia of Torus: " + str(tor.ProductOfInertia))
print("Principal directions of Torus: " + str(tor.PrincipalDirections))
print("Principal moments of Torus: " + str(tor.PrincipalMoments))
print("Radius of giration of Torus: " + str(tor.RadiiOfGyration))

