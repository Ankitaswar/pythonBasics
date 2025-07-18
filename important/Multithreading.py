from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)  # they will not collide
t2.start()

t1.join()
t2.join()

print("Bye")  #main thread --> after join now it will wait for t1 and t2 then it will run

