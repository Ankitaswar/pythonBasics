# import array as arr
from array import *

vals = array('i', [5,9,8,4])  #Type - Value
print(vals, vals.buffer_info())  #address of the array
print(vals.typecode)
vals.reverse()
print(vals.tolist())

for i in range(len(vals)):
    print(vals[i] , end= " ")
print()

for e in vals:
    print(e , end= " ")
print()

newArr = array(vals.typecode, (a*a for a in vals))
for e in newArr:
    print( e , end= " ")
print()

# vals = array('str', ['a', 'e', 'e'])
# for e in vals:
#     print(e , end= " ")


