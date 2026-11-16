numbers = []
for x in range(10): # 0 ile 10 arasındaki sayıları yazdırı.
    numbers.append(x) # 0 ile 10 arasındaki sayıları numbers listesine ekler.
print(numbers)

numbers = [x for x in range(10)] # 0 ile 10 arasındaki sayıları bir listeye atar.
print(numbers)

for x in range(10):
    print(x**2)

numbers = [x**2 for x in range(10)]
print(numbers)

numbers = [x*x for x in range(10) if x % 3 == 0]  # x sayısının karesinin 3 e tam bölünen sayılarını yazdırır.
print(numbers)

myString = 'Hello'
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1983, 1999, 2008, 1986]
ages = [2019-year for year in years]
print(ages)

result = [x if x % 2 == 0 else 'TEK' for x in range(1, 10)]
print(result)

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print(result)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)
