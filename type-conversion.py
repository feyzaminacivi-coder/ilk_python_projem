'''
x = input('1.sayi: ') 
y = input('2.sayi: ')

print(x + y) #string olarak toplama yapar

print(type(x))
print(type(y))

toplam = int(x) + int(y) #int() fonksiyonu ile string ifadeleri integer'a çevirip toplama işlemi yapar

print(toplam) 
'''


x = 5              #int
y = 2.5            #float
name = 'Çınar!'    #str(string) (isim)demek
isOnline = True    #bool            (Çevrimiçi mi?) demek 

#print(type(x))
#print(type(y))
#print(type(name))
#print(type(isOnline))

#Type Conversion (Tip Dnüşümü)

#int to float

# x = 5
# x = float(x)
# print(x)
# print(type(x))   

#float to int

# y = int(y)
# print(y)
# print(type(y))      #Yukarıdaki flaot tipindeki y değişkeni int tipine dönüştürüldü ve artık 2 olarak yazdırıldı.

# result = x + y
# print(result)
# print(type(result))      #5+2.5 = 7.5 float tipinde bir sonuç verir.

#result = str(x) + str(y)
#print(result)              #5+2.5 = 52.5 string tipinde bir sonuç verir.
#print(type(result))         #result değişkeni string tipinde bir sonuç verir.

#bool to string

# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))    #True ifadesi string tipine dönüştürüldü ve artık True olarak yazdırıldı.

#bool to int

isOnline = False   # sıfır (0) ve True (1) olarak int tipine dönüştürülebilir.

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))  #True ifadesi int tipine dönüştürüldü ve artık 1 olarak yazdırıldı. False ifadesi int tipine dönüştürüldüğünde 0 olarak yazdırılır.

