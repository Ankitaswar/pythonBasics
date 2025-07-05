
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 18

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1  = Student('Ankit', 24)
# s1.show()
#
# lap1 = s1.lap
# lap2 = s1.lap
#
# print(id(lap1))
# print(id(lap2))

s2  = Student('Vikas', 89)

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))

s1.show()

l1 = Student.Laptop() #object of inner class