f = open("MyData", 'r')
# print(f.readline(), end ="")
# print(f.readline(4), end ="")

f1 = open('abc', 'w') # if file not exist this will create a new file
f1.write("Something")
f1.write("Laptop")

# a - > append -> we want to add data

#copy
for data in f:
    f1.write(data)

#for Image
# f = open('img.jpg', 'rb')
# f1 = open("MyPic.JPG", 'wb')
# for i in f:
#     f1.write(i)

