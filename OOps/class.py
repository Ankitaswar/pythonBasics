class Computer:
    def config(self):
        print("8gb 15 1TB")

com1 = Computer()
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

#OR
com1.config()
com2.config()
