import json
# f = open("file.json", "w", encoding="utf-8")
# json.dump("салим", f, ensure_ascii=False)
# f.close()

# f = open("file.json", "w", encoding="utf-8")
# c = json.load(f)
# f.close()
# print(c)
#
#
# class Person:
#     def __init__(self, imya, vozrast): # магический метод(инициализации)
#         self.name = imya
#         self.age= vozrast
#
#
#     def __str__(self):
#         return f"Я {self.name} и мне {self.age} лит"
#
# chelovek = Person("Данис", 29) # создание объекта класса Person
# chelovek1 = Person("Виталий", 32) # создание объекта класса Person
#
# print(chelovek1.age)
# print(chelovek.name)
# print(chelovek)


# class Klass:
#     def __init__(self, i, f, v):
#         self.name = i
#         self.fam = f
#         self.age = v
#
#     def __str__(self):
#         return f"Имя:{self.name}\n Фамилия:{self.fam}\n Возраст:{self.age}\n"
#
#     def greet(self):
#         return f"Привет, меня зовут {self.name} {self.fam} мне {self.age} лет"
#
# man=Klass("кэфтемэ", "тяги бархатные", 993)
# man1=Klass("naruto", "zxc", 7)
#
# print(man.greet())
import random


# ЗАДАЧА 2
# nums = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
# print(nums)
import random
class Person:
    def __init__(self, imyau, familia, voz):
        self.name = imyau
        self.femiliya = familia
        self.vozrast = voz
        self.grades = [random.randint(2, 5) for _ in range(random.randint(5, 10))]
        self.srbal = sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Возраст: {self.vozrast}\nИмя: {self.name}\nФамилия: {self.femiliya}"

    def greet(self):
        return f"Привет, меня зовут {self.name}, мне {self.vozrast} лет."


chel = Person("Антон", "Бананов", 15)
chel2 = Person("Володя", "Приколов", 17)
print(chel.grades, chel.srbal)

