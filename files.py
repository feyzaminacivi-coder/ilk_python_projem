# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (write) yazma modu. 
# Dosyayı konumda oluşturur.
# Dosya içeriğini siler ve yeniden ekleme yapar. 

# file = open("newfile.txt","w")
# file.close()

#file = open("C:/users/feyzamina/destkop/newfile.txt","w")

file = open("newfile.txt","w")
file.write("Feyza mina")
file.close()


# "a" : (append) ekleme. Dosya konumda yoksa oluşturur.


file.write("feyza")
file.close()

# "x" : (Create) oluşturma. Dosya zaten varsa hata verir.

file = open("newfile2.txt","x",encoding='utf-8')

# "r" : (Read) okuma. varsayılan. dosya konumda yoksa hata verir.

