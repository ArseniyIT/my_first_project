# f = open("Восьмй бэ сегодян дежурный класс.txt", "w", encoding="utf-8")  # создаст если нет, перезапишет если есть
# f.write("Hellow orld\n")
# f.write("Я славянин")
# f.close()

# f = open("Восьмй бэ сегодян дежурный класс.txt", "r", encoding="utf-8")
# # считываем содержимое файла и помещаем в content
# # content = f.read()  # ЛИБО ТАК
# content = f.readlines()  # ЛИБО ТАК
# print(content)
# for logarifm in content:
#     print(logarifm.rstrip())  # убираем пустоты(перенос строки) справа
# f.close()


# ЗАДАЧА 1
# name = input("Название файла: ")
# f = open(name + ".txt", "w", encoding="utf-8")
# msg = input("Содержимое: ")
# while msg != "":  # пока не пустая строка
#     f.write(msg + "\n")  # + перенос строки
#     msg = input("Содержимое: ")

# Задача 2
# a = input("Введите имя файла: ")
# f = open(a, 'r')
# content = f.readlines()
# v = len(content)
# for i in range(v):
#     print(f"{i+1})",content[i].strip())

# ЗАДАЧА 3
f = open("zxc.txt", "r", encoding="utf-8")
text = f.readlines()
f.close()
count = 0
while text != []:  # пока не вытащены все линии
    elements = text[:3]
    count += 1
    f = open(str(count) + ".txt", "w", encoding="utf-8")
    for i in elements:  # элемент из троек
        f.write(i)
    f.close()
    del text[:3]