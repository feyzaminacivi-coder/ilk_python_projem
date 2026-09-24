"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müştrei doğum yılı
    Müşteri adres bilgisi
    Müşteri yaşı
    """
musteriAdi = 'Elif'
musteriSoyad = 'Civi'
musteriAdSoyad = musteriAdi + ' ' + musteriSoyad
print(musteriAdSoyad)
musteriCinsiyet = True #Kadin
musteriTcKimlik = '41564157535'
musteriDogumYili = 1989
musteriAdres = 'Istanbul Kadikoy'
musteriYasi = 2026 - musteriDogumYili

"""
    2-Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.

    Siparis 1 => 110    TL
    Siparis 2 => 1100.5 TL
    Siparis 3 => 356.95 TL

    """

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95

toplamSiparis = siparis1 + siparis2 + siparis3

print("Toplam Sipariş Tutari: ",toplamSiparis)


