def func1():
    print("Func 1", __name__)

def func2():
    print("Func 2")

def main():
    func2()
    func1()


if __name__ == '__main__':
    main()

