import os
import datetime

result = dir(os)
result = os.name
result = os.getcwd()

# klasör değştirme
#os.chdir('C://')
#os.chdir('..')
#os.chdir('..//..')

# klasör oluşturma
#os.mkdir("newdirectory")
#os.makedirs("newdirector/yeniklasör")
# os.rename("newdirectory","yeniklasör")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasör/newdirectory")


# listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)



# etkin dizin öğrenme
#os.mkdir = os.getcwd()

# result = os.stat("_datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime)    # oluşturulma zamanı
# result = datetime.datetime.fromtimestamp(result.st_atime)    # son erişim tarihi  
# result = datetime.datetime.fromtimestamp(result.st_mtime)    # değiştirilme tarihi

#os.system("notepad.exe")

# path



print(result)

