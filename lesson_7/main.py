# ZeroDivisionError
# print(50/0)

# TypeError
# x = 1 + "one"

# IndexError
# lst = ["один", 1, "Антон"]
# lst[3]

# exit code
# 0 - значит все хороше
# 1 - ошибка
# -1 - прерывание программы пользователем

# NameError
# print(x)

# try:
#     number = int(input("введи чило: "))
#     x = 5 / number
#     print(x)
# except ZeroDivisionError: # ловим исключение, делить на ноль незя
#     print("1000-8")
# except ValueError: # если ввёдем букввы
#     print("хачу цифирки")
# except Exception: # обработка любой ошибки
#     print("one error and you are erroring")

# try:
#     name = input("введите имя: ")
#     if name == "Антон":
#         raise Exception("отпути не путю")
# except Exception as error_m: #складываем исключения в error_m
#     print("наказана", error_m)
# else: # иначе(если не выхываличсь исключения)
#     print("ну вот такое имя мона")
# finally: #сработает в любом случеае
#     print("ня")
#
# print("я отработав")

# try:
#     number = int(input("введите число"))
#     x = 5 / number
# except Exception:
#     pass #затычка, заглушка
# if 3 == 3:
#     pass # TODO: не забудь дописать и купить молока.
#
# temperature = 365 # я кеоментарий
# print()
# def summa(numbers):
#     return sum(numbers)
#
# print(summa([1, 2, 3])) # печатаем рез-т функциюю при [1, 2, 3]
# assert summa([1, 2]) == 3
# assert summa([1, 2]) == 4

# assertionError
