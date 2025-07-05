# instance, class, static method

class Student:
    school = 'KV2'
    def __init__(self, m1, m2, m3):
        self.m1 =m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  #instance method  : accessor
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self): # #instance method  : accessor
        return self.m1

    def set_m1(self, value):  ##instance method  : mutator
        self.m1 = value

    @classmethod
    def getSchoolName(cls):  #class Method
        print(cls.school)

    @staticmethod
    def info():
        print("This is student class")

s1 = Student(2,3,4)
print(s1.avg())

Student.getSchoolName()

Student.info()



