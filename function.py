def greet():
    print("Hello Good Morning")

def add(a,b):
    print(a+b)

def mul(a,b):
    return a*b

def sub_add(a,b):
    c = a+b
    d = a*b
    return c, d

greet()
add(2,3)
res = mul(2,3)
print(res)

res1, res2 = sub_add(4,6)
print(res1, ' ', res2)

