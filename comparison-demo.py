# 1- Girilen 2 sayıdan hangisi büyüktür?

'''
sayi1 = int(input())
sayi2 = int(input())

if sayi1 > sayi2:
    print(f"{sayi1}, {sayi2}'den büyüktür.")
else:
    print(f"{sayi1}, {sayi2}'den küçüktür.")

'''

'''
a = int(input('a: '))
b = int(input('b: '))

result = (a > b)
print(result)

'''



# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

'''
vize1 = float(input('1.vize notunu giriniz: '))
vize2 = float(input('2.vize notunu giriniz: '))
final = float(input('1.final notunu giriniz: '))

vize_ort = (vize1 + vize2) / 2
ort = (vize_ort * 0.60) + (final * 0.40)
print(f"not ortalamanız: {ort} ve dersten geçme durumunuz: {ort>=50}")
'''

# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdır.



# 3- Girilen bir sayını tek mi çift mi olduğunu yazdırın.

'''
sayi = int(input('Sayıyı giriniz: '))
if sayi %2 == 0:
    print(f"Gridğiniz {sayi} değeri çifttir.")
else:
    print(f"Girdiğiniz {sayi} değeri tektir.")
'''

'''
sayi = int(input('sayıyı girin: '))
tekcift = (sayi % 2 == 0)

print(f'girilen sayının çift olma durumu: {tekcift}')
'''


# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

'''
sayi = int(input('Sayıyı girin: '))
if sayi > 0:
    print("sayı pozitif")
elif sayi < 0:
    print("sayı negatif")
else:
    print("sayı 0'dır.")
'''

'''
sayi = int(input('sayı: '))
pozitif_mi = (sayi > 0)

print(f"girilen sayının pozitif olma durumu: {pozitif_mi}")
'''


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#        (email: email@sadikturan.com parola: abc123)

email = "email@sadikturan.com"
parola = "abc123"

EMAİL = input('email girin: ')
PAROLA = input('parola girin: ')

if email == EMAİL:
    if parola == PAROLA:
        print('Giriş başarılı')
else:
    print('Giriş başarısız')







