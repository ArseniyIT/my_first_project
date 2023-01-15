# def abdul(): #объявление функции
#     print("hello_world")
#
# #-------------------------------
#
# abdul() # вызов функции

# def plus(number1, chislo2):
#     result = number1 + chislo2
#     return result # то что вернет функция
#
# x = plus(5, 3) # вызов функции сс аргументом. результат записан в переменную
# plus(chislo2=3, number1=23) # указывания конкретных аргументов

# def baran(name):
#     if name = "dima":
#     return True
#
# if baran("pupok"): # если функция вернет True
#     print("eto dima")
# else:
#     print("eto ne dima")

# def check(list):
#     sort = sorted(list) #сортировка списка
#     if list == sort: #если list отсортирован
#         return True
#
# list = [1, 2, 3, 4, 5]
# print(check(list))
# if check(list) == True
#     print("писок по возрастанию")
# else:
#     print("список не отсортирован")

# def find_longest(list):
#     spisok2 = []
#     for i in list:
#         spisok2.append(len(i))
#     maxy = max(spisok2)
#     ind = spisok2.index(maxy)
#     return list[ind]
#
#
# spisok = ["Баран", "Дом", "Дед", "Диван", "Танго"]
#
# print(find_longest(spisok))
#
#
# find_longest(spisok)

# def min_max(chisla):
#     minim = chisla[0]
#     maxim = chisla[0]
#     for i in chisla:
#         if i > maxim:
#             maxim = i
#         elif i < minim:
#             minim = i
#     print(maxim,minim)
#
# chisla = [1,2,3,4,5,6,7]
# print(min_max(chisla))

# def is_prime(abdul):
#     for i in range(2, abdul+1):
#         if i == abdul:
#             return True
#         if abdul % i == 0:
#             break
#
#
# if is_prime(523):
#     print("да")
# else:
#     print("net")


# def join(baran:list, razdel:str)->str:
#     resick = ""
#     for i in baran:
#         resick += 1 + razdel
#     return resick
#
# listick = ["da", "net", "ok"]
# print(join(listick, ">"))


def  factorial(chislo):
    x = 1
    for i in range(2,chislo+1):
        x *= i
    return x



print(factorial(15))
