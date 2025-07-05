a=5
b=6

# M1
temp = a
a = b
b = temp
print(a)
print(b)
print("---------- Required extra varibale")


#M2
a1=5 # 3bit
b1=6 #3bit
a1 = a1+b1  # 11 -> 4Bit  -> wasting one bit
b1 = a1 - b1
a1 = a1 -b1
print(a1)
print(b1)
print("---------- Wasting extra bit")

#M3
a2=5 # 3bit
b2=6 #3bit
a2 = a2 ^ b2  #
b2 = a2 ^ b2
a2 = a2 ^ b2
print(a2)
print(b2)
print("-----No Extra bit required")

#M4 - Amazing about python
a3,b3 = 5,6
a3,b3 = b3, a3  # work in one line -> use stack and use rotation concept (ROT_TWO)
print(a3)
print(b3)