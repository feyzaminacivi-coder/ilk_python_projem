website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1- 'course' karakter dizisinde kaç karakter bulunmaktadır?
result = len(course)
lenght = len(website)

#2- 'website' içinden www karakterlerini alın.
result = website[7:10]
print(result)

#3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[lenght - 3:lenght] 
print(result)

#4- 'course' içinden ilk 15 ve son 15 karakteri alın.
result = course[0:15]
result = course[:15]
result = course[-15:]
print(result)


#5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::]    #Baştan sona yazdırır.
result = course[::-1]   #Sonradan başa yazdırır.
print(result)


#s = '12345' * 5
#print(s[::5])



name, surname ,age, job = 'Bora' ,'Yılmaz', 32, 'mühendis'

result = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job 
print(result)

#int ifade string birleştirme işlemine tabi tutulamaz bu yüzden stringe çevrilir.


#6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'

#7- 'Hello world"ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)


#8- 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc'*3)




# print(len(course))
# print(website[7:10])
# print(website[19:22])
# print(course[:15])
# print(course[-15:])
# print(course[::-1])
# print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")



