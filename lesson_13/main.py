
# a = [0,4,2,2,2,3,3,1,4,5,3,2,3,1,4,2,3,4,1,4,1,2]
# for i in range(0, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')
# print()
# for i in range(0, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# import random
#
# b = []
# a = [1, 2, 1, 8, 9, 7, 5, 6, 3, 8, 1, 9, 6]
#
# for i in (a):
#     if i in b:
#         print('yes')
#     else:
#         print('no')
#         b.append(i)
# from random import randint
# print(max([randint(0, 500) for i in range(100)]))

# циклы
# while и for
# x = 5
# while x == 5:
#     pass
# while True:  # бесконечный цикл
#     print(123)
#
# while False:  # код недосягаем
#     print("я антон")


# for
# phrase = "фраза"
# for toyota_supra in phrase: # 1-й способ: перебор в переменной
#     print(toyota_supra)

# for jojo in range(5): # сработает 5 раз
# for jojo in range(0,5): # то же самое
#     print(jojo)

# множества

# empty_dict = dict() #единственный способ создания пустого множества
# set1 = {1, 2, 3} # литеральный способ
# print(type(set1))
# set0 = {1, 1, 1, 2} # 1) ПОВТОРЕНИЯ ИСКЛЮЧЕНЫ
# print(set0)
# set00 = {"А", "Б", "Ц"}  # 2) неупорядочный тип данных
# print(set00)
# set000 = {1, [2, 3]} # список во множестве
#TypeError -> нельзя помещать изменяемыва типы данных во множество
# немутабельный типы данный = неизменяемый
# int, float, bool, str. tuple

# Операции на множествах
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
#
# # объединение
#
# print(set1.union(set2))
# print(set1 | set2) # одно и то же
#
# print(set1.intersection(set2))
# print(set1 & set2) # амперсанд
#
# # разность
# print(set1.difference(set2))
# print(set1 - set2)
#
# # симметрическая разность
# print(set1.symmetric_difference_update(set2))
# print(set1^set2

from random import randint
#
# lst = []
# for _ in range(5):
#     lst.append(randint(1, 5))
# print(lst)
# unique = set(lst) # список -> множество
# print(unique)
# print(f"{len(unique)}шт. {unique}")

r_start = 0
r_end  = 10000 # 10_000 то же самое что и 10000
size = randint(100, 1000)