fruits = { 'orange', 'apple', 'banana'}

#print(fruits[0])  indexlenemez.

for x in fruits:
    print(x)

fruits.add('cherry')  #yeni eleman ekler.
fruits.update(['mango','grape','apple'])   #liste ekler.
#zaten içinde var olan eleman tekrarlanmaz ve sadece bir kez yazılır.

fruits.remove('mango')
fruits.discard('apple')  #elemanı siler.

fruits.pop()  #herhangi bir elemanı siler. 
fruits.clear()  #bütün elemanları siler.


print(fruits)

myList = [1,2,5,4,4,2,1]

print(myList)
print(set(myList))

