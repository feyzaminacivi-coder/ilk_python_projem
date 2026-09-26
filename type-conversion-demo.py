'''

    Daire Alanı  : pi * (r ** 2)
    Daire Çevresi: 2 * pi * r

    *Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r: 3.14)
'''

# r = 3.14
# pi = 3.14

# alan = pi * (r ** 2)
# cevre = 2 * pi * r

# print("Dairenin Alani: ", alan)
# print("Dairenin Cevresi: ", cevre)


# r = input("yarıçapı giriniz: ")
# pi = 3.14

# alan = pi * float(r) ** 2
# cevre = 2 * pi * float(r)

# print(alan)
# print(cevre)


pi = 3.14

r = float(input("yarı çap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r

# print("alan:", alan)
# print("çevre:", cevre)       #Burada alan ve çevreyi yazdırmak için print() fonksiyonu kullanıldı.

#print("alan: " + alan + " çevre: " + cevre)   #Burada alan ve çevreyi yazdırmak için print() fonksiyonu kullanıldı.Ancak burada alan ve çevre değişkenleri float tipinde olduğu için string tipine dönüştürülmesi gerekir. Aksi takdirde TypeError hatası alırsınız.

#Float tipindeki alan ve çevre değişkenlerini string tipine dönüştürmek için str() fonksiyonu kullanılır.

print("alan: " + str(alan) + " çevre: " + str(cevre))    #Bu komutu kullanarak alan ve çevreyi yazdırabilirsiniz.

#Kısacası float tipindeki değişkenlerde string birleştirme işlemi yapılamaz. Bu yüzden float tipindeki değişkenleri string tipine dönüştürmek gerekir.


