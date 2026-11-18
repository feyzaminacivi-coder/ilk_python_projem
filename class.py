# class

# class Person:
#     pass
#     # class attributes
#     address = 'no information'

#     # constructor(yapıcı metod)
#     def __init__(self, name, year):
#         pass

#         # object attributes
#         self.name = name
#         self.year = year
#         print('init metodu çalıştı.')

#     # instance methods
#     def intro(self):
#         print('Hello There. I am ' + self.name)
#     def calculateAge(self):
#         return 2019 - self.year
    


# # objets (instance)

# p1 = Person(name = 'ali', year =1990)
# p2 = Person(name = 'yağmur',year = 1995)

# p1.intro()
# p2.intro()

# print(f'adım: {p1.name} ve yaşım: {p1.calculateAge()}')
# print(f'adım: {p2.name} ve yaşım: {p2.calculateAge()}')


# # updating
# p1.name = 'ahmet'
# p1.address = 'kocaeli'


# # accessing object attributes
# print(f'name: {p1.name} year: {p1.year} address: {p1.address}')
# print(f'name: {p2.name} year: {p2.year} address: {p2.address}')


# print(p1)   #  <__main__.Person object at 0x000001B0C7F38590>
# print(p2)
# print(type(p1))
# print(type(p2))
# print(p1 == p2)


class Circle:
    #Class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2*self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)

c1 = Circle()  # yarıçap = 1
c2 = Circle(5)

print(f'c1 : alan = {c1.alan_hesapla()} çevre : {c1.cevre_hesapla}')
print(f'c2 : alan = {c2.alan_hesapla()} çevre : {c2.cevre_hesapla}')



