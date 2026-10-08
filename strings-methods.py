message = "Hello There. My name is Feyza. I am learning Python programming."

#message = message.upper() #Bütün harfleri büyük yapar.
#message = message.lower() #Bütün harfleri küçük yapar.
#message = message.title() #Her kelimenin ilk harfini büyük yapar.
#message = message.capitalize() #Sadece ilk harfi büyük yapar.

#message = message.strip() #Başındaki ve sonundaki boşlukları siler.
#message = message.split() #Cümleyi kelimelere ayırır ve listeye çevirir.
#message = message.split(".") #Cümleyi noktalara göre ayırır ve listeye çevirir.
#message = '*'.join(message) #Listeyi tekrar cümleye çevirmek için kullanılır. Her kelimenin arasına * koyar.

#index = message.find("Feyza") #İlgili kelimenin cümledeki indexini verir. Eğer kelime yoksa -1 döndürür.
#isFound = message.startswith("H") #Cümle belirtilen harf ile başlıyorsa True, başlamıyorsa False döndürür.
#isFound = message.endswith("g.") #Cümle belirtilen harf ile bitiyorsa True, bitmiyorsa False döndürür.

#message = message.replace("Feyza", "Mina") #Cümledeki ilgili kelimeyi değiştirir.
#message = message.replace(" ", "*") #Cümledeki boşlukları değiştirir.
#message = message.replace('ç', 'c').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').replace('ğ', 'g').replace('ı', 'i') #Türkçe karakterleri İngilizce karakterlere çevirir.

message = message.center(50,"*") #Cümleyi belirtilen karakter ile ortalar.



#print(isFound)

print(message)
#print(message[0]) #Listenin ilk elemanını yazdırır.
#print(message[2])



