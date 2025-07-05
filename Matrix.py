from numpy import *
arr = array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
])

print(arr.ndim)  # print dimension
print(arr.shape) # no of rows and column
print(arr.size)

#Convert 2D arr into 1D arr
arr1 = arr.flatten()  # 1D
print(arr1)

#Convert into 3D arr
arr2 = arr1.reshape(3,4) # 3 rows and 4 col
print(arr2)

arr3 = arr1.reshape(2,2,3) # 3 rows and 4 col
print(arr3)


#Matrices
m = matrix('1 2 3; 6 4 5; 1 6 7')

print(m)  # now we can perform more operation

print(diagonal(m))
print(m.min())

m2 = matrix('1 2 3; 6 8 5; 2 6 7')
m3 = m * m2 # matrices multiplication direclty done in python
print(m3)

