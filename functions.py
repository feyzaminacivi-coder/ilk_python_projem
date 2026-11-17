def sayHello(name = 'user'):  # parametre belirtimediğinde Hello user yazdırır.
    return'Hello ' + name  # fonksiyona geri gönderilmesini sağlar.

# sayHello('Çınar')
# sayHello('Ada')
# sayHello()   #parametre belirtilmediği için çalışmaz.

msg = sayHello('Çınar')

print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)

print(result)

def yasHesapla(dogumYili):
    return 2026 - dogumYili

ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)

print(ageCinar, ageAda, ageSena)

def EmekliligeKcYilKaldi(dogumYili, isim):

    '''
DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı
INPUT: Doğum yılı
OUTPUT: Hesaplanan yıl bilgisi

    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f'emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz.')

EmekliligeKcYilKaldi(1983, 'Ali')
EmekliligeKcYilKaldi(1950, 'Ahmet')
EmekliligeKcYilKaldi(1974, 'Yağmur')

help(EmekliligeKcYilKaldi)

list = [1,2,3]

print(help(list.append))   # listenin sonuna obje eklemek için kullanıldığını söyler.


