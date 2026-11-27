# def usalma(number):
#     # two = usalma(2)
#     # three = usalma(3)

#     def inner(power):
#         return number ** power

#     return inner

# two = usalma(2)
# three = usalma(3)

# print(two(2))
# print(three(3))



# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
#     return inner

# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpim

toplama = islem("toplama")
print(toplama(1,3,5,7))

carpim = islem("carpim")
print(carpim(1,2,3))


