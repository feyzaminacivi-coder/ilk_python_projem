numbers =[1,2,3,4,5]

for num in numbers:
    print(num)      #'num' değişkeni her döngüde 'numbers' listesindeki bir öğeyi temssil eder ve bu öğe ekrana yazdırılır.

names = ['çınar', 'sadık', 'sena']
for name in names:
    print(f'my name is {name}')     #'name' değişkeni her döngüde 'names' listesindeki bir öğeyi temsil eder ve bu öğe ekrana yazdırılır.

name = 'Feyza Mina'

for n in name:
    print(n)   #'n' değişkeni her döngüde 'name' stringindeki bir karakteri temsil eder ve bu karakter ekrana yazdırılır.


tuple = (1,2,3,4,5)
for t in tuple:
    print(t)  #'t' değşkeni her döngüde 'tuple' içindeki bir öğeyi temsil eder ve bu öğe ekrana yazdırılır.

tuples = [(1,2),(3,4),(5,6)]

for t in tuples:
    print(t) #'t' değişkeni her döngüde 'tuples' lisetsi içindeki bir öğeyi temsil eder ve bu öğe ekrana yazdırılır.

tuples = [(1,2),(3,4),(5,6)]

for a, b in tuples:
    print(f'{a} and {b}')

    tuples = [(1,2),(3,4),(5,6)]

for a in tuples:
    print(a)  #'a' değişkeni her döngüde 'tuples' lisetsi içindeki bir öğeyi temsil eder ve bu öğe ekrana yazdırılır.

d = {'k1':1, 'k2':2, 'k3':3}

for key, value in d.items():
    print(f'{key}: {value}') #'key' ve 'value' değişkenleri her döngüde 'd' sözlüğündeki anahtarları ve değerleri temsil eder ve bu öğeler ekrana yazdırılır.

