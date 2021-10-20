from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

pmatrx = aDouble(10 ,1, 3, 10, 5, 5, 10, 10, 3, 15, 1, 0, 15, 5, 0, 15 ,10, 0, 20 ,1, 0, 20 , 5, -1, 20 ,10 ,0, 25 ,1, 0, 25, 5, 0, 25 ,10, 0)

mesh1 = acad.model.Add3DMesh(4, 3, pmatrx)

print("Coordinates of the mesh:", end='')
print(mesh1.Coordinates)
print("Is mesh one is closed in M direction: " + str(mesh1.MClose))
print("Density of mesh in M direction: " + str(mesh1.MDensity))
print("Number of vertices in M direction: " + str(mesh1.MVertexCount))
print("Is mesh one is closed in N direction: " + str(mesh1.NClose))
print("Density of mesh in N direction: " + str(mesh1.NDensity))
print("Number of vertices in N direction: " + str(mesh1.NVertexCount))
