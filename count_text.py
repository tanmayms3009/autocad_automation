from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

count_a1 = 0 
for i in acad.iter_objects(object_name_or_list=None, block=None, limit=None, dont_cast=False):
    if i == "A1":
        count_a1+=1

print(count_a1)