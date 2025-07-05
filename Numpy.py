# to work with multidimensional array, perform scientific calculation

from numpy import *

arr2D = array([[1,2,3,4], [5,6,7,8]])
print(arr2D)

for i in range(len(arr2D)):
    for j in range(len(arr2D[0])):
        print(arr2D[i][j], end= " ")
    print()

#Ways to create array --> array(), linspace(), logspace(), arange(), zeros(), ones()
arr = array([1,2,3,4])
arr1 = array([1,2,3,4,5.0])
print(arr.dtype) # int64
print(arr1.dtype) #float64
print(arr1)

arr = array([1,2,3,4], float)
print(arr)

#linspace
arr = linspace(0, 16, 20)  # num-> divided into 20 parts
print(arr)

arr = linspace(0, 16)  # num-> divided into 20 parts
print(arr)

#arange
arr = arange(1, 15, 2)
print(arr)


#logspace
arr = logspace(1,40,5)
print(arr)
print('%.2f' %arr[4])

#zeros --> efficient
arr = zeros(5) # by default float
arr = zeros(5, int)
print(arr)

#ones
arr = ones(5, int)
arr = ones(5)
print(arr)

#-----------

arr = array([1,2,3,4,5])
arr = arr + 5
print(arr)

arr1 = array([6,7,8,9,10])
arr2 = arr + arr1
print(arr2)

print(sin(arr1))
print("sqrt", sqrt(arr1))
print(sum(arr1))

print(concatenate([arr, arr1]))


#-------
arr1 = array([1,2,4,5,6])
arr2 = arr1

#both arr are same and pointing to same address
print(arr1 , " ", arr2)
print(id(arr1), " ", id(arr2))


#but we want copying arr but a new one
arr3 = arr1.view()
print(id(arr1), " ", id(arr3))

#Shallow copy : it got changed in both the array
arr1[1] = 90
print(arr1)
print(arr3)


#Deep Copy
arr1 = array([1,2,4,5,6])
arr3 = arr1.copy()
print(id(arr1), " ", id(arr3))

#Deep copy : it not got changed in both the array
arr1[1] = 90
print(arr1)
print(arr3)


