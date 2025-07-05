#python bi-default not support abstract classes but we have module ABC module
#abstract class have atleat one abstract method

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    pass

class Mac(Computer):

    def process(self):
        print("Mac")

#we cannot create object of abstract class

# c1 = Computer() # thorw error

# l1 = Laptop()
# Can't instantiate abstract class Laptop with abstract method process -> we need to define
# we need override the process method

m1 = Mac() # now it will work as we override the process method
