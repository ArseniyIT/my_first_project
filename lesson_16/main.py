# primer1 = lambda a, b: a + b + 1 # лямбда функция поместили в переменную
#
# print(primer1(5, 10)) # вызов функции не отличается
# answer = "Д"
# exit_triger = lambda yn: True if yn == "Д" else False
# print(exit_triger(answer))

# ГЕНЕРАТОР СПИСКА (list compresehension)
# lst = []
# for i in range(1,6):
#     lst.append(i)
# print(lst)
#
# lst2 = [i for i in range(1,6)]
# 1. всегда в []
# 2. for i in ... -> сколько элементов в списке
# 3. всё что перед or -> сам элемент списка

# за да ча 1
# c2f = lambda c: 9/5 * c + 32
# f2c = lambda f: (f-32) * 5/9
# c2k = lambda c: 273.15 + c
# k2c = lambda k: k - 273.15
# f2k = lambda f: c2k(f2c(f))
# degree = 203
# print(c2k(degree))

# # за да ча 2
# import random
# kubi = int(input("кол-во кубов?"))
# dices = [random.randint(1,6) for i in range(kubi)]
# print(dices)

# from random import choice
# chars = [list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
#          list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя"),
#          list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
#          list("abcdefghijklmnopqrstuvwxyz"),
#          list("1234567890")
#         ]
# lst = []
# for i in range(6):
#      lst.append(choice(choice(chars))) # случайно элемент в список добавили
# code = "".join(lst)
# silka = "https://youtu.be/Z-Ew7ieSOLw"
# d = {}
# # d = {"https://youtu.be/Z-Ew7ieSOLw" : "roflan"}
# if silka in d:
#     print("эта ссылка уже есть ->", d[silka])
# else:
#     d[silka] = code
#     print("ссылка добавлена влт ее код ->", d[silka])

# за да ча 4
import math
a = 2
b = 1024
yy1 = lambda a, b : b - a
print(yy1(a, b))

yy2 = lambda a, b : b + a

yy3 = lambda a, b : b / a

yy4 = lambda a, b : b * a

yy5 = lambda a, b : a / b

firamir = lambda x : -x if x<0 else x
print(firamir(-5))


logoped = lambda a, b : math.log(b, a)
print(logoped(2, 1024))