def greeting(name):
    print('hello ', name)

#print(greeting('ali))
#print(greeting)

# sayHello = greeting

# print(sayHello)
# print(greeting)

# del sayHello
# print(greeting)
# print(sayHello)

# encapsulation
def outer(num1):
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    num2 = inner_increment(num1)

outer(10)

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    
    if not number >= 0:
        raise ValueError("number must be zero or position")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)
print(factorial(4))

