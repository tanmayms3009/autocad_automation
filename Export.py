from pyautocad import Autocad

acad = Autocad(create_if_not_exists=True)

ss = acad.doc.SelectionSets.Add("ss2")

acad.doc.Export("C:\\Users\\91998\\OneDrive\\Desktop\\Drawings\\d1", "dxf", ss)

#COMING UP WITH METHODS TO EXPORT DRAWING IN OTHER FORMATS
