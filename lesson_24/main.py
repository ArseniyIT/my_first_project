# class Human:
#     def __init__(self): #магический метод
#         self.height = 993 # паблик данных
#         self.__money = 0.3 # приват данных
#
#     def mamatvoya(self): #обычный метод
#         return "сам такой"
#
#     def ipotek(self):
#         if self.__money > 50 and self.__normal_height(): # юзаем приват в классе
#             return True
#         else:
#             return "попрошу у мамы твоей"
#
#     def __normal_height(self): # приватный метод
#         if self.height > 100 and self.height < 200:
#             return True
#
# chelovek = Human()
# # print(chelovek.height)
# # print(chelovek.mamatvoya())
#
# print(chelovek.height) # паблик можно выводить
# chelovek.height += 7
#
# # print(chelovek.__money) # приват нельзя выводить
# # chelovek.__money = 5 # приват(паблик) можно менять?
# # chelovek.__money = chelovek.__money = 5
# # print(chelovek.__money)
#
# chelovek._Human__money +=6


# class Car:
#     def __init__(self, color, type, year):
#         self.cvet = color
#         self.tip = type
#         self.let = year
#
#     def zavodim(self):
#         return "Автомобиль заведен"
#
#     def glusim(self):
#         return "Автомобиль заглушен"
#
#     def god(self):
#         return masina.let
#
#     def tipok(self):
#         return masina.tip
#
#     def svet(self):
#         return masina.cvet
#
# masina = Car("Черный с тонером", "Джип крузак 300", 2022)
# print(masina.zavodim())
# print(masina.glusim())
# print(masina.god())
# print(masina.tipok())
# print(masina.svet())

# import string
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.__lang = lang
#         self.__letters = string.ascii_lowercase
#
#
#     def print(self):
#         return self.__letters
#
#     def letters_num(self):
#         return len(self.__letters)
#
# a = Alphabet("eng", string.ascii_lowercase)


import datetime
class Samtakoi:

    def __init__(self):
        self.__h, self.__m, self.__s = datetime.datetime.now().strftime("%H:%M:%S").split()
        self.__h, self.__m, self.__s = int(self.__h), int(self.__m), int(self.__s)

    def chas(self):
        self.__h += 1

    def vavod(self):
        return f"{str(self.__h).rjust()}:{str(self.__m).rjust()}:{str(self.__s).rjust()}"

    def minuta(self):
        self.__m += 1

    def secunda(self):
        self.__s += 1

b = Samtakoi()
print(b.vavod())