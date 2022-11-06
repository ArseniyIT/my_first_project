# git config --global url. "https://github.com/".insteadOF git@github.com
# git config --global url. "https://".insteadOF git:// - от ошибки
#
# import random
# import time
#
# print("Время пострелять.")
#
# is_game = "y"
# while is_game == "y"
#     time.sleep(1)
#     print("*Заряжаем револвер*")
#     time.sleep(3)
#     print("*Раскручиваем барабан револьвера*")
#     time.sleep(2)
#     print(3)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(1)
#     time.sleep(1)
#     print("*Выстрел*")
#
#     slots = [1, 2, 3, 4, 5, 6]
#     patron = random.choice(slots) # .choice - выбрать случайно
#     our = random.choice(slots)
#
#     if patron == our:
#         print("Есть пробитее")
#         is_game = "n"
#     else:
#         print("Повезло-повезло")
#         x = input("Играем дальше? y - да, n - нет")
#         if x == "n":
#             is_game = "n"

# ЦИКЛЫ

# for
# lst = ["Егор", "Арсений", "Дима", "Артем"]
# for antoha in lst:
#     print(antoha, end="+_+")
#
# for i in range (0, 10):
#     print("Питон лав")
#
# while
# while x != 10:
#     print(hex(x += 1)) #  то же самое что и x = x + 1
#
# word = input("Введи слово: ")
# while word:
#     print(word)
#     word = word[:-1]
#
# x = int(input("Введите циферку: "))
# while x: # если != 0 то работает
#     x -= 1
#     if x % 2 == 0:
#         print(x, end=" ")
#
# x = int(input("Введите циферку: "))
# step = 0
# while x != 1:
#     step += 1
#     if x % 2 == 0:
#         print(f"{step})", end=" ")
#         print(x, "* 3  + 1 =", end=" ")
#         x = x // 2
#     else:
#         print(f"{step})", end=" ")
#         print(x, " / 2 =", end=" ")
#         x = 3 * x + 1
#     print(x)
# print("Шагов:", step)
