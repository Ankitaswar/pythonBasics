from array import *

arr = array('i', [])

n = int(input("Enter the size of the arr"))

for i in range(n):
    x = int(input(f"Enter the element {i}: "))
    arr.append(x)

print(arr.tolist())


# find index of the given value
val = int(input("Enter the Value"))
k =0

for i in arr:
    if i==val:
        print(k)
        break
    k += 1
else:
    print("Not Found")

#Direct
print(arr.index(val)) # this will throw error if not found