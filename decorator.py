#without changing impl of the existing func

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner_func(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return inner_func

new_div = smart_div(div)

new_div(2,4)