# x = 10
# while x > 0:
# x = x - 2
# print(x)
#
# lst = [0, 1, 2, 3, 4, 5]
#
# for megarush in lst: #пробегаемся по всем элементам списка
#     print(megarush)
#
# for megarush in tange(0, 10 + 1):
#     print(megarush)

# x1 = int(input("ведите число  "))
# x2 = int(input("ведите число  "))
# #
# # while x1 <= x2:
# #     print(x1, end=" ")
# #     x1 += 1
#
# for coolrush in range(x1, x2 + 1):
#     print(coolrush)
#
# number = int(input("Введите кол-во ярусов-->"))
# while True:
#     charm = input("введи символ").strip()
#     if len(charm.strip()) == 1:
#         break # получив нужное выходим из while
#     else:
#         print("you error")
# for megarush in range(1, number + 1):
#     print(" " * (number - megarush), end="")
#     print(charm * megarush, end="")
#
#     print(charm * megarush) # правая половина + перенос строчки
#
# x = int(input("ведите число: "))
# for tablica in range(1, 10 + 1):
#     print(x, "x", tablica, "=", x * tablica)

x1 = int(input("кол-во сиволов с строке"))
x2 = int(input("кол-во строк"))

for _ in range(x2): # 0 do x2 (не вкл.)
    print("#" * x1)