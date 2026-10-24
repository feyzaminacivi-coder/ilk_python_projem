# 1- "Bmw, Mercedes, Opel,Mazda" elemanlarına sahip bir liste oluşturunuz.

arabalar = ['Bmw','Mercedes','Opel','Mazda']
 

# 2- Liste kaç elemanlıdır?

#result = len(arabalar)
#print(result)


# 3- Listenin ilk ve son elemanı nedir?

#result = arabalar[0]
#result = arabalar[3]
#result = arabalar[-1]


#print(result)



# 4- Mazda değerini Toyota ile değiştirin.

lists = "Bmw, Mercedes, Opel,Mazda"

#list = lists.replace("Mazda","Toyota")
#print(list)

#arabalar[-1] = 'Toyota'
#result = arabalar
#print(result)


# 5- Mercedes listenin bir elemanı mıdır?

#result = lists.find("Mercedes")
#print(result)

#result = 'Mercedes' in arabalar 
#print(result) 

# 6- Listenin -2 indexindeki değer nedir?

#print(list([-2]))

#result = arabalar[-2] 



# 7- Listenin ilk 3 elemanını alın.

#result = arabalar[0:3]
#result = arabalar[:3]
#result = arabalar[-2:]
#print(result)  

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

#arabalar[-2:] = ['Toyota','Renault'] 
#result = arabalar
#print(result)


# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

#result = arabalar + ['Audi', 'Nissan'] 
#print(result) 



# 10- Listenin son elemanını silin.

# del arabalar[-1] 
# result = arabalar
# print(result)


# 11- Liste elemanlarını tersten yazdırın.

result = arabalar[::-1]  #Tersten yazar.
print(result)


# 12- Aşağıdaki verileri bir liste içinde saklayınız.

    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    # studentC: Ahmet Turan 1998, (80,70,90)


studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1999, [80,80,70]]
studentC = ["Ahmet", "Turan", 1998, [80,70,90]]

students = [(studentA), (studentB), (studentC)]
print(students)

# 13- Liste elemanlarını ekrana yazdırınız.

# result = studentA[0]
# result = studentB[1]
# result = studentC[3][1]

result = f"{studentA[0]} {studentA[1]} ({2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"



print(result)
