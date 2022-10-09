# aplhabet = "АБВГДЕЁЖЗИЙКЛМНОПОРСТ"
#
# print(aplhabet[::-1]) # вывод в обратную сторону
#
# phrase = "антон"
# print(phrase.upper()) # поднять в рехний регистр
# print(phrase.lower()) # опустить в нижний регистр
#
# phrase1 = "я КаРта, я ФраЗа, Я кВраТ"
# print(phrase1.capitalize())
#
# famaliya = input("Фамилия: ")
# imya = input("Имя: ")
# otchestvo = input("Отчество: ")
#
# print(famaliya, imya[0] + ".", otchestvo[0] + ".")
# print(f"{famaliya} {imya[0]}. {otchestvo[0]}.")
#
# familiya1 = input("Фамилия: ").capitalize()
# imya1 = input("Имя: ").capitalize()
# otchestvo1 = input("Отчество: ").capitalize()
# print(familiya1, imya1[0] + ".", otchestvo1[0] + ".")
#
# x = input()
# print(x.count('a')) # кол-во смол а
# print(x.lower().count('a')) # кол-во смол и биг а
#
# x = input("Введите фразу, разделяя слова запятыми: ")
# lst = x.split(",")
# lst.pop(0)
# print(lst)#split - разделяет, расколоть
# #.remove("Вова") - удалить элемент Вова
# #.pop(3) - удалить под инедксом 3
#
# phrase = input("Введи фразу:")
# find = input("Что меняем: ")
# replace = input("На что меняем: ")
#
# print(phrase.replace(find, replace))
#
# phrase = input("Введите фразу: ")
# print(phrase.replace("ё", "е"))
#
# alphabet = {
#      " ": " ",
#      "а": "a",
#      "б": "b",
#      "в": "v",
#      "г": "g",
#      "д": "d",
#      "е": "e",
#      "ё": "yo",
#      "ж": "zh",
#  }
# x = input("Введи фразу для транситерации: ")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva]
# print(rus)
#
# alphabet = {
#       " ": " ",
#       "а": "a",
#       "б": "b",
#       "в": "v",
#       "г": "g",
#   }
# x = input("Введи фразу для транситерации: ")
# rus = ""
# for bukva in x:
#     rus = rus + alphabet[bukva] + ""
# print[rus]
#
# email = input("введите почту: ")
# print(emali.split("@"))
# login = emali.split("@")[0]
# domain = emali.split("@")[-1]
# print("Логин: ", login)
# print("Домейн: ", domain)