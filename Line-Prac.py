#########################################################
#Setup
from pyautocad import Autocad, APoint
import math
import xlsxwriter
import re

#Name Autocad Function:
acad = Autocad()

#Convert List to Tuple:
def convert(list):
    return tuple(list)

#Calculate Length of Line
def length():
    p1 = l1.StartPoint
    p2 = l1.EndPoint

    res = tuple(map(lambda i, j: i - j, p2, p1))
    res2 = tuple(map(lambda i: i*i, res))

    len = round(math.sqrt(res2[0]+res2[1]),2)
    dim = acad.model.AddDimAligned(APoint(p1), APoint(p2), APoint(1, 1, 0))

    print("Length of Line: " + str(len))
    return round(len, 2)

######################################################

#Create Excel File:

excel = input("Enter Excel File name: ")
excel_sheet =  input("Enter Excel File Sheet name: ")

#####################################################

#Draw Line, Get Length, Draw Dimensions

select = input("1: To Draw Line or 2. Already Drawn: ")

#Draw and work:
if select == "1":
    nl = int(input("Enter number of Lines to be added: "))
    wb = xlsxwriter.Workbook(excel + ".xlsx")
    s1 = wb.add_worksheet(excel_sheet)
    cell_no = input("Enter Cell Number: ")
    match = re.match(r"([a-z]+)([0-9]+)", cell_no, re.I)
    if match:
        c = match.groups()
    cxa = c[0]
    cxn = int(c[1])+1
    for l in range(nl+1): #To print description with 1
        if l != 0:
            lp1 = []
            lp2 = []
            #iterating till the range
            for i in range(0, 3):
                ele = float(input("Enter values for x, y, z for Start point of Line No. " + str(l) + ": "))
                lp1.append(ele) # adding the element
                convert(lp1)
            print(lp1)
            for j in range(0, 3):
                ele = float(input("Enter values for x, y, z for End point of Line No. " + str(l) + ": "))
                lp2.append(ele) # adding the element
                convert(lp1)
            print(lp2)
            l1 = acad.model.AddLine(APoint(lp1),APoint(lp2))
            lmn = length() 
            print(lmn)
            s1.write((str(cxa) + str(cxn)), lmn)
            cxn += 1
    wb.close()

#Working with predrawn lines:

elif select == "2":
    l1 = acad.iter_objects(object_name_or_list="AcDbLine", dont_cast=True, limit=None, block=acad.doc.Layouts.item(2).Block)
    wb = xlsxwriter.Workbook(excel + ".xlsx")
    s1 = wb.add_worksheet(excel_sheet)
    cell_no = input("Enter Cell Number: ")
    match = re.match(r"([a-z]+)([0-9]+)", cell_no, re.I)
    if match:
        c = match.groups()
    cxa = c[0]
    cxn = int(c[1])+1
    for l1 in l1:
        print(l1.ObjectName)
        lmn = length()
        print(lmn)
        s1.write((str(cxa) + str(cxn)), lmn)
        cxn += 1
    wb.close()
###################################################################
