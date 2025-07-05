print(int.__add__(2,3))
print(str.__add__('5','6'))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        res = Student(m1, m2)
        return res

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.m1}, {self.m2}" #it will return string

s1 = Student(58,34)
s2 = Student(100,40)

s3 = s1 + s2  #Student class don't know what is + there we need do overload this as __add__()
print(s3.m1, s3.m2)

if s1 > s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s1)


