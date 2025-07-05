from cgi import print_environ_usage


class Person:
    def __init__(self):
        self.name = 'Ankit'
        self.age = 28

    def update(self):
        self.age = 34

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

p1 = Person()
p1.age = 89
p2 = Person()

if p1.compare(p2):
    print("Object are same")
else:
    print("not Same")


p1.name = 'Vikas'
p1.age = 99
print(p1.name, p1.age)

p1.update()
print(p1.name, p1.age)