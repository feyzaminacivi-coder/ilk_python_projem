# def my_decorator(func):
#     def wrapper():
#         print("fonksiyondan önceki işlemler")
#         func()
#         print("fonkssiyondan sonraki işlemler")
#     return wrapper

# @my_decorator
# def sayHello(name):
#     print("hello",name)
# sayHello("ali")

# def sayGreeting():
#     print("greeting")


# sayHello = my_decorator(sayHello)
# sayGreeting = my_decorator(sayGreeting)
# sayHello()


import math
import time

def usalma(a,b):
    start  = time.time()
    time.sleep(1)

    print(math.pow(a,b))

    finish = time.time()
    print("fonksiyon "+str(finish-start)+" saniye sürdü.")

def faktöriyel(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))

    finish = time.time()
    print("fonksiyon "+str(finish-start)+" saniye sürdü.")

usalma(2,3)

    

