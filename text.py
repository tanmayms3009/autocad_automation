from pyautocad import Autocad, APoint, aDouble

acad = Autocad()

# Text, Insertion Point, Text Height
t1 = acad.model.AddText("Hello", APoint(75, 50), 25)

print("Text content: " + t1.TextString)
print("Text style: " + t1.StyleName)
print("Text insertion point: ", end=" " )
print(t1.InsertionPoint)
print("Text alignment: " + str(t1.Alignment))
print("Text alignment point: " + str(t1.TextAlignmentPoint))
print("Text height: " + str(t1.Height))
print("Text rotation: " + str(t1.Rotation))
print("Text scale factor: " + str(t1.ScaleFactor)) 
print("Is the text upside down: " + str(t1.UpsideDown))


#Insertion Point, Width, Text
mt1 = acad.model.AddMText(APoint(275, 150), 100, "This is auotocad text")
mt1.Height = 25

print("Text width: " + str(mt1.Width))

