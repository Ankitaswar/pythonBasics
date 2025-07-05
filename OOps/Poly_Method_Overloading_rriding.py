#__add__() can diff/no or arguments are diff
#Method Overloading : class have 2method with same Name but diff no of parameter  --> but python do not have
# this functionality as we can't define two method with same name.
#to achieve this: -->
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None, b=None, c=None):
        s =0
        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s

s1 = Student(12,13)

print(s1.sum(12,13,14)) # work
print(s1.sum(12,13)) # throw error --> Sol : use None and check cond
print(s1.sum(12))


#Method Overriding : Same Name and Same Parameter : Inheritance
class A:

    def show(self):
        print("In a show")

class B(A):
    # pass

    def show(self):
        print("In B show")

a1 = A()
a1.show()
a2 = B()
a2.show()



