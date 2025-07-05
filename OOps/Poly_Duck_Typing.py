class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyOwnEditor:
    def execute(self):
        print("Spell Checking")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()


ide = Pycharm()
ide1 = MyOwnEditor()
lap1 = Laptop()
lap1.code(ide)  # also has execute method
print("----------------")
lap1.code(ide1)  # also has execute method

#Not matter what you are passing the thing is it should have that method as in this
# case execute is the method