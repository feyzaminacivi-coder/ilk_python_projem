'''

    ogrenciler = {
        '120' : {
            'ad' : 'Ali' ,
            'soyad' : 'Yılaz' ,
            'telefon' : '532 000 00 01'
            },
        '125' : {
                'ad' : 'Can' ,
                'soyad' : 'Korkmaz' ,
                'telefon' : '532 000 00 02'
                },
        '128' : {
            'ad' : 'Volkan' ,
            'soyad' : 'Yükselen' ,
            'telefon' : '532 000 00 03'
            },
     }
      
     
     1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

     2-Öğrenci numarası kullanıcıdan alıp ilgili öğrenci bilgisine gönderin.

     '''


#  1-

ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("telefon no: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad':surname,
#     'telefon':phone
# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("telefon no: ")


ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})


number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyadı: ")
phone = input("telefon no: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})




print(ogrenciler)


#  2-

print('*'*50)


ogrNo = input('ogrenci no: ')
ogrenci = ogrenciler[number]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']}ve telefonu ise {ogrenci['telefon']}")





