from pyautocad import Autocad, APoint, aDouble
from math import *

acad = Autocad(create_if_not_exists=True)


def helix():
    obj = acad.iter_objects(limit=None, block=acad.doc.Layouts.item(2).Block)
    for obj in obj:
        print("Type of object: " + obj.ObjectName)
        if obj.ObjectName == "AcDbHelix":
            print("Top radius of helix: " + str(round(obj.TopRadius,2)))
            print("Base radius of helix: " + str(round(obj.BaseRadius,2)))
            print("Helix constrain: " + str(round(obj.constrain,2)))
            print("Height of helix: " + str(round(obj.Height,2)))
            print("Center point of helix: ")
            print(obj.Position)
            print("Total length of helix: " + str(round(obj.TotalLength,2)))
            print("Number fo turns helix took to complete: " + str(round(obj.Turns,2)))
            print("Slope of turns: " + str(round(obj.TurnSlope,2)))
            print("Height of single turn: " + str(round(obj.TurnHeight,2)))
            print("Twist of the helix: " +  str(round(obj.Twist,2)))

            obj.Move(APoint(obj.Position), APoint(1500, 1000))
            obj.TopRadius = 450
            obj.BaseRadius = 700
            obj.Height = 500
            obj.Twist = 1

            print("Top radius of helix: " + str(round(obj.TopRadius,2)))
            print("Base radius of helix: " + str(round(obj.BaseRadius,2)))
            print("Helix constrain: " + str(round(obj.constrain,2)))
            print("Height of helix: " + str(round(obj.Height,2)))
            print("Center point of helix: ")
            print(obj.Position)
            print("Total length of helix: " + str(round(obj.TotalLength,2)))
            print("Number fo turns helix took to complete: " + str(round(obj.Turns,2)))
            print("Slope of turns: " + str(round(obj.TurnSlope,2)))
            print("Height of single turn: " + str(round(obj.TurnHeight,2)))
            print("Twist of the helix: " +  str(round(obj.Twist,2)))

helix()




