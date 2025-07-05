def change_val(x):
    print(id(x))
    x = 10  # reassign x to new int
    print(id(x))

a = 5
print(id(a))
change_val(a)
print(a)  # ➡️ 5 (not changed)

#Types of argument :

# 1.Position Argument
def fun(a,b):
    print(a+b)

fun(2,3)
# 2. Keyword
def person(name, age):
    print(name, age)

person('ankit', 24)
person(age=22, name='vikas')

# 3. Default
def person(name, age=18):
    print(name, age)

person('vandana')
person('vandana', 20)

# 4. Variable length
def sum(a, *data):
    print(a)
    c=0
    print(data)  # tuple
    for i in data:
        c = c +i
    print(c)

sum(2,3,4,5)

#---------------------------------------- **kwargs
def human(name, *data):
    print(data)

human('navin', 28, 'Mumbai', 9516635649)

def human1(name, **data):
    print(data)
    for key, val in data.items():
        print(key,':', val)

human1('navin',age=28,city= 'Mumbai', phoneNo = 9516635649)




