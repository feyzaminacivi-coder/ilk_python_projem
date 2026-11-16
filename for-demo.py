sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır?

for sayi in sayilar:
    if sayi % 3 == 0:
        print(f'{sayi} sayısı 3 ün tam katıdır.')
              
# 2- Sayilar listesinde sayıların toplamı kaçtır?

toplam = 0
for sayi in sayilar:
    toplam += sayi
print(f'Sayıların toplamı: {toplam}')   #'print' i  for döngüsünün içine yazarsak her adımda toplamı yazar dışına yazarasak en son yazar.



# 3- Sayilar listesindeki tek sayıların karesini alınız.

for sayi in sayilar:
    if sayi % 2 == 1:
        print(f'{sayi} sayısının karesi: {sayi**2}')


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']

#4- Şehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler:
    if len(sehir) < 5:
        print(f'{sehir} şehri 5 karakterden az.')
    elif len(sehir) ==5:
        print(f'{sehir} şehri 5 karaktere eşittir.')
    else:
        print(f'{sehir} şehri 5 karakterden fazladır.')




urunler = [
    {'name': 'samsung s6', 'price': '3000'},
    {'name': 'samsung s7', 'price': '4000'},
    {'name': 'samsung s8', 'price': '5000'},
    {'name': 'samsung s9', 'price': '6000'},
    {'name': 'samsung s10', 'price': '7000'}
]


# 5- Ürünlerin fiyatları toplamı nedir?

toplam = 0
for urun in urunler:
    toplam += int(urun['price'])
print(f'Ürünlerin fiyatları toplamı: {toplam}')

# 6- Ürünerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(f'{urun["name"]} - {urun["price"]}')

