website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40Saat)"


# 1-  'Hello World' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

#Kendi çözümüm:
# result = 'Hello World'
# result = result.replace("H", " ")
# result = result.replace("d", " ")
# result = result.strip()
# print(result)

#result = 'Hello World'.strip()  #Boşlukları siler.
#result = 'Hello World'.lstrip()  #Solundaki boşlukları siler.
#result = 'Hello World'.rstrip()   #Sağındaki boşlukları siler.

#result = website.lstrip('/:pth')  #Belirttiğimiz ifadeyi siler.
#print(result)

#result = 'www.sadikturan.com'.strip('w.moc')




# 2-  'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

#Kendi çözümüm:
# result = website[11:25] 
# print(result)

#result = 'www.sadikturan.com'.strip('w.moc')


# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

#Kendi çözümüm:
#result = course.lower()
#print(result)

# 4-  'website' içinde kaç tane a karakteri vardır?

#Kendi çözümüm:
#result = website.count("a")  #count() metodu, bir karakter dizisinde belirli bir karakterin kaç kez geçtiğini saymak için kullanılır. Bu örnekte, "website" değişkenindeki "a" karakterinin sayısını bulmak için kullanılmıştır.
#print(result)

#result = website.count('www',0,10)    #0 ile 10. karakterler arasında belirttiğimiz ifadenin olup olmadığı sonucunu alırız.



# 5-  'website' "www" ile başlayıp com ile bitiyor mu?

#Kendi çözümüm:
# result = website.startswith("www") and website.endswith("com") #startswith() metodu, bir karakter dizisinin belirli bir karakter dizisiyle başlayıp başlamadığını kontrol eder. endswith() metodu ise bir karakter dizisinin belirli bir karakter dizisiyle bitip bitmediğini kontrol eder. Bu örnekte, "website" değişkeninin "www" ile başlayıp "com" ile bitip bitmediği kontrol edilmiştir.
# print(result)

# 6-  'webiste' içinde '.com' ifadesi var mı? 

#Kendi çözümüm:
#result = website.find(".com")  #varsa index numarasını yazar.
#print(result)


# 7- 'course' içindeki karakterlerin hepsi alfabetik mi?

#Kendi çözümüm:
#result = course.isalpha() #isalpha() metodu, bir karakter dizisinin yalnızca alfabetik karakterlerden oluşup oluşmadığını kontrol eder. Eğer tüm karakterler alfabetik ise True, aksi takdirde False döndürür. Bu örnekte, "course" değişkenindeki karakterlerin hepsinin alfabetik olup olmadığı kontrol edilmiştir.
# print(result)

#result = course.isdigit()  #verilen değerlerin rakam olup olmadığını kontrol eder.
#result = '123'.isdigit() 
#print(result)


# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

#Kendi çözümüm:
#result = 'Contents'.center(50, "*") #center() metodu, bir karakter dizisini belirtilen genişlikte ortalar ve boşlukları veya belirtilen karakterleri ekler. Bu örnekte, 'Contents' ifadesi 50 karakter genişliğinde ortalanmış ve sağ ve soluna '*' karakterleri eklenmiştir.
#result = 'contents'.ljust(50,"*") 
#result = 'contents'.rjust(50,"*") 
#print(result)


# 9- 'course' karakter dizisindeki tüm boşluk karaterlerini "-" ile değiştirin.

#Kendi çözümüm:
#result = course.replace(" ", "-") #replace() metodu, bir karakter dizisindeki belirli bir karakteri veya karakter dizisini başka bir karakter veya karakter dizisi ile değiştirir. Bu örnekte, "course" değişkenindeki tüm boşluk karakterleri "-" ile değiştirilmiştir.
# print(result)
# result = course.replace(' ','-',5) #Sadece 5 tane koyar.
# result = course.replace(' ','')  #Tüm boşluk karakterlerini siler.



# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.

#Kendi çözümüm:
#result = 'Hello World'.replace("World", "There") #replace() metodu, bir karakter dizisindeki belirli bir karakteri veya karakter dizisini başka bir karakter veya karakter dizisi ile değiştirir.
#print(result)

# 11- 'course' karakte dizisini boşluk karakterlerinden ayırın.

#Kendi çözümüm:
result = course.split(' ')
result = result[5]


print(result)






















