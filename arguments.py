# def changeName(n):
#     n = 'ada'

# name = 'yiğit'

# changeName(name)
# print(name)


# def change(n):
#     n[0] = 'İstanbul'  # 0. indexteki elemanı istanbul yapar.

# sehirler = ['ankara','izmir']  

# change(sehirler[:])

# change(sehirler)

# print(sehirler)   # değiştirlimiş listeyi yazdırır.

# n = sehirler[:]  # kopyalama işlemi yapar.  # slicing işlemi

# n[0] = 'istanbul'

# print(sehirler)

# def add(a, b, c = 0):
#     return sum((a, b, c))

# print(add(10, 20))
# print(add(10, 20, 30))

# # 6 dan fazla parametre ekleneceği zaman:

# def add(*params):
#     print(params[0])  # tuple şeklinde yazdırır ,istenen indexteki değeri yazar.
#     print(params[1])
#     return sum((params))

# print(add(10,20,30,40,50,60))

# # sum fonksiyonu kullanılmazsa

# def add(*params):
#     sum = 0

#     for n in params:
#         sum = sum + n
#     return sum


def displayUser(**args):
    print(type(args))    #  <class 'dict'>
    for key, value in args.items():
        print(' {} is {}' .format(key,value))


displayUser(name='Çınar', age = 2, city = 'İstanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli', phone = '123123')
displayUser(name = 'Yiğit', age = 14, city = 'ankara', phone = '123132', email = 'yiğit@gmail.com')

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    


myFunc(10, 20, 30, 40, 50, key1 = 'value 1', key2 = 'value 2')


