i=1

while i <= 10:
    j = 1
    print("Hello: ", end="")
    while j<=5:
        print("Inner Loop: ", end="")
        j += 1
    i += 1
    print()


print("outSide the loop Now")