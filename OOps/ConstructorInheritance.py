#MRO : Method Resolution Order

class A:
    def __init__(self):
        print("Constructor of A")

    def featureA1(self):
        print("Feature 1 Working")

    def featureA2(self):
        print("Feature 2 Working")


class B(A):  #Single Level

    def featureB1(self):
        print("Feature 3 Working")

    def featurB2(self):
        print("Feature 4 Working")


class C(A):
    def __init__(self):
        super().__init__()  #calling init of superclass i.e A
        print("C Constructor")

    def featureC1(self):
        print("Feature 3 Working")

    def featurC2(self):
        print("Feature 4 Working")

# = A() #Constructor Called

#b1 = B() ##Constructor Called of A because B Don't Have their own constructor

#c1 = C() # now it will only it's constructor

#c1 = C()  # i will call cons of A then C as we're using super()

class A_Sub:
    def __init__(self):
        print("Constructor of A_Sub")

    def featureA1(self):
        print("Feature A_Sub 1 Working")

    def featureA2(self):
        print("Feature A_Sub 2 Working")

class E(A, A_Sub):  #Multiple Inheritance
    def __init__(self):  # prefer left superclass : A  (Left -> right)
        super().__init__()  #calling A only it is unfair : Solution MRO
        print('Constructor of E')

e = E() # call left superclass then own constructor
e.featureA1()  #left -> right therefore it will call featureA1 method of right superclass : This is MRO

#we can call methods also using super
