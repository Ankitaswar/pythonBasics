#instance, class(static) variable

class Car:
    wheels = 4 #class/static variable and namespace

    def __init__(self):
        self.mil = 10  #Instance variable and namespace
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil = 8
print(c1.mil, c1.com, c1.wheels)

Car.wheels = 5
print(c1.mil, c1.com, c1.wheels)