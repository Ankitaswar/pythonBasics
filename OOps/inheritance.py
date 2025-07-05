class A:
    def featureA1(self):
        print("Feature 1 Working")

    def featureA2(self):
        print("Feature 2 Working")


class B(A):  #Single Level
    def featureB1(self):
        print("Feature 3 Working")

    def featurB2(self):
        print("Feature 4 Working")

class C(B):  #Multilevel
    def featureC1(self):
        print("Feature 3 Working")

class A_Sub:
    def featureA_Sub1(self):
        print("Feature 3 Working")

class D(A, B):  #Multiple
    def featureD1(self):
        print("Feature 3 Working")

b1 = B()
b1.feature1()
b1.featur4()

c1 = C()

d1 = D()
