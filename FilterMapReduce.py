from functools import reduce
nums = [3,2,6,7,4,6,2,9]

# def isEven(n):
#     return  n%2 == 0
# even = list(filter(isEven, nums))

even = list(filter(lambda n : n%2==0, nums))
print(even)

double = list(map(lambda n : n*2 ,even))
print(double)

sum = reduce(lambda a,b: a+b, double)
print(sum)