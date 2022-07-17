from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

acad.doc.Import("C:\\Users\\91998\\OneDrive\\Desktop\\Drawings\\d1.dxf", aDouble(0, 0, 0), 1)