from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

ip = APoint(0, 0, 0)
b1 = acad.doc.Blocks.Add(ip, "Test_block_1")

pl = b1.AddPolyline(aDouble(0, 0, 0, 10000, 0, 0, 10000, 5000, 0, 0, 5000, 0, 0, 0, 0))
l = b1.AddLine(APoint(0, 250, 0), APoint(10000, 250, 0))

block_ref1 = acad.model.InsertBlock(APoint(50, 50, 0), "Test_block_1", 1, 1, 1, 0)

#PROPERTIES_BLOCKS
print("Object Name: " + b1.ObjectName)
print("Name of Block: " + b1.Name)
print("Native units of measures for the Block: ", end="")
print(b1.Units)
print("Is scaling allowed for the block ? ", end="")
print(b1.BlockScaling)
print("Is the block explodable ? ", end="")
print(b1.Explodable)
print("Is the block dynamic ? ", end="")
print(b1.IsDynamicBlock)

#METHODS
print(b1.Item)
#b1.Delete()    

#Properties of BlockReference
print("Object Name: " + block_ref1.ObjectName)
print("Block Name: " + block_ref1.Name)
print("Original Block Name: " + block_ref1.EffectiveName)

print("Entity Transparency: ", end="")
print(block_ref1.EntityTransparency)

print("Does the Block contain any Attributes: ", end="")
print(block_ref1.HasAttributes)

print("Insertion Point: ", end="")
print(block_ref1.InsertionPoint)

print("Insert units saved with Blocks: ", end="")
print(block_ref1.InsUnits)

print("Conversion factor between Block units and drawing units: ", end="")
print(block_ref1.InsUnitsFactor)

print("Is the Block dynamic ? ", end="")
print(block_ref1.IsDynamicBlock)

print("Layer: " + block_ref1.Layer)

print("Line type: " + block_ref1.Linetype)

print("Line type scale: ")
print(block_ref1.LinetypeScale)

print("Line weight: ")
print(block_ref1.Lineweight)

print("Rotation angle for the block: ")
print(block_ref1.Lineweight)

#Scale factors
print("X Scale factor of block: ", end="")
print(block_ref1.XEffectiveScaleFactor)

print("X Scale factor for block or external reference (xref): ", end="")
print(block_ref1.XScaleFactor)

print("Y Scale factor of block: ", end="")
print(block_ref1.YEffectiveScaleFactor)

print("Y Scale factor for block or external reference (xref): ", end="")
print(block_ref1.YScaleFactor)

print("Z Scale factor of block: ", end="")
print(block_ref1.ZEffectiveScaleFactor)

print("Z Scale factor for block or external reference (xref): ", end="")
print(block_ref1.ZScaleFactor)