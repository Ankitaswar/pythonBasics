a = 10

def func():
    a = 15
    print(a)


def func1():
    print(a)

def func2():
    global a
    a = 15 # now this is global
    print(a)

def func3():
    global a
    a = 15 # now this is global
    print(a)
    #now we cant create a new local variable as a beacuse now a will treat as global variable

b = 10
print("Address", id(b))
def func4():
    # x = globals() # it will give all the global variable available
    x = globals()['b']
    print("in a func", id(x))
    print('in a func4',a)

    globals()['b'] = 15 #we are changing global variable withour affecting the local variable


func()
func1()
func2()
func3()
func4()

print("Outside", a)  # by adding global a will get 15 now
print("Outside", b)  # by adding global a will get 15 now