def factorial(n):
    if n==0 and n<=0:
        print(1)
    else:
        f = 1
        for i in range(1, n+1):
            f = f*i;
    return f

print(factorial(5))

#Recusrsion
def facRec(n):
    if n == 0:
        return 1

    return n * facRec(n-1)


print(facRec(5))

