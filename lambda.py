def spuare(num):
    return num ** 2
# bu fonksiyonu aynı satır içinde yazabiliriz

def square(num): return num ** 2

result = square(2)

print(result)   # 4

# liste varsa

#def square(num): return num ** 2
#square = lambda num: num ** 2

numbers = [1, 3, 5, 9, 10, 4]

#result = map(square, numbers)
#result = list(map(square, numbers))
#result = list(map(lambda num: num ** 2, numbers))

result = square(3)

# for item in map(square, numbers):
#     print(item)

#def check_even(num):
 #   return num%2==0
check_even = lambda num: num%2==0



#result = list(filter(check_even, numbers))  #   [10, 4]
#result = list(filter(lambda num: num%2==0, numbers))
#result = list(filter(check_even, numbers))

result = check_even(numbers[2])

print(result)   # <map object at 0x0000027D388799C0>




