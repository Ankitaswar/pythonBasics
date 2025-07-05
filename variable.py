x =2
print(x + 3)
print(x)

name = 'Ankit'
print(name)
print(name[1])
print(name[-1])  #start from the end of the string  len(name)(5) -1 = 4 index
print(name[0:2])
print(name[1:])
print(name[:2])
print(name[3:12]) # print upto last not give error
# name[0:3] = 'PA'   #String is unmutable

print(len(name))

#Address of Varibale
print(id(name))

#if the variable has same data then the address is same
a =10
b = a
print(id(a))
print(id(b))
print(id(10))

a = 9
print(id(a)) #now diff add as we change the data

#In python we cannot create constant
print(type(a))

