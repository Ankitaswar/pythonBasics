def fibbnacci(n):
    a=0
    b=1
    if n<=0:
        print("Invalid Number")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2,n):
        c = a+b
        # if(c > n):
        #     print(b)
        #     break
        a = b
        b = c



fibbnacci(100)