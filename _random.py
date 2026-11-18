import random

#result = dir(random)
#result = help(random)

result = random.random()  # 0.0 -1.0 aradında her zaman farklı bir sayı üretir.
result = random.random() * 100  # üretilen sayılar her seferinde 100 ile çarpılır.
result = int(random.uniform(10,100))
result = random.randint(1,100)

greeting = 'Hello There'
names = ['ali','yağmur','deniz','cenk','ahmet','efe']
result = names[random.randint(0, len(names) - 1)]
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)  # listeden rastgele 3 sayıyı getirir.
result = random.sample(names, 3)

print(result)