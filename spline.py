from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)

p1 = aDouble(0, 0, 0, 42, 25, 0, 100, -15, 0, 155, 45, 0)
sp1 = acad.model.AddSpline(p1, APoint(2, 2, 0), APoint(50, 75, 0))

print(sp1.Closed)
print(sp1.Closed2)
print("Control Points:")
print(sp1.ControlPoints)
print(sp1.Degree)
print(sp1.Degree2)
print(sp1.StartTangent)
print(sp1.EndTangent)
print(sp1.FitPoints)
print(sp1.FitTolerance)
print(sp1.IsPeriodic)
print(sp1.IsPlanar)
print(sp1.IsRational)
print(sp1.KnotParameterization)
print(sp1.Knots)
print(sp1.NumberOfControlPoints)
print(sp1.NumberOfFitPoints)
print(sp1.SplineFrame)
print(sp1.SplineMethod)