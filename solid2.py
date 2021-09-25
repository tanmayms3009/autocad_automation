from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

c1 = acad.model.AddCircle(APoint(100, 100, 0), 100)

r1 = acad.model.AddRegion(c1)

es = acad.model.AddExtrudedSolid(r1, 200, 60)

# AddExtrudedSolidAlongPath(Profile, Path)