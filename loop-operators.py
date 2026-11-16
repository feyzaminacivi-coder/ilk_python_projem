# list = [1,2,3]

# for item in range(2,10):   # 2 den 10 a kadar olan sayıları yazdırır.
#     print(item)

# print(list(range(50,100,20)))  # 50'den 100'e kadar 20'şer artırarak sayıları yazdırı.


#enumerate() fonksiyonu, bir iterable (tekrarlanabilir) nesneyi (örneğin bir liste veya bir dize) alır.
# index = 0
# greeting = 'Hello There!'

# for letter in greeting:
#     print(f"index: {index}, letter: {letter}")
#     index += 1

#enumerate() fonksiyonu ile aynı işlemi yapabilriz:

# greeting = 'Hello There!'

# for index, letter in enumerate(greeting):   # greeting stringindeki her bir harfi ve indexini yazdırır.
#     print(f"index: {index}, letter: {letter}")

# for index, item in enumerate(range(10,20)):  # 10 ile 20 arasındaki sayıları ve indexlerini yazdırır.
#     print(f"index: {index}, item: {item}")

# zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3))) # list1, list2 ve list3 ü birleştirir.

for item in zip(list1,list2,list3): # list1, list2 ve list3 ü birleştirir ve her bir elemanı yazdırır.
    print(item)

for a,b,c in zip(list1,list2,list3): #list1, list2 ve list3 ü birleştirir ve her bir elemanı ayrı ayrı yazdırır.
    print(f'a: {a},b: {b},c: {c}')
    


