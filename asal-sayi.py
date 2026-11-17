'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
**Asal sayı 1 ve kendisi hariç tam böleni olmayan
  sayılara denir.
'''

sayi = int(input('sayı: '))
asalMi = True

if sayi == 1:
    print('asal değildir.')

for i in range(2, sayi):
    if sayi % i == 0:
        asalMi = False
        break
if asalMi:
    print('asal sayıdır.')
else:
    print('asal değildir.')
    
