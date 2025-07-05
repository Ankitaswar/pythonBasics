available = 5
buy = 10
i=1
while i< buy:
    if i > available:
        print("Out of Stock")
        break

    print("Candy")
    i +=1

print("Bye")

i=1
for i in range(1, 101):
    if i%3 ==0 or i%5 ==0 :
        continue
    print(i , end=" ")
print()

i=1
for i in range(1, 101):
    if i%2 !=0 :
        pass
    else:
        print(i , end=" ")


for i in range(5):
    if i==3:
        continue
    print("Hello", i)

    if i == 4:
        pass


def func():
    pass  # i don't know how to implement

class Human:
    pass