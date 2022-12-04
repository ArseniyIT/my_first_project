# a = int(input("first number"))
# b = int(input("first number"))
# lst = []
#
# for aaa in range(a + 1, b):
#     lst.append(aaa * 2)
# print(lst)

# x = input("vvod: ")
# lst = x.split(" ")
# print(lst)
# lst.reverse()
# print(lst)

# number = input("число: ")
# chet = 0
# nechet = 0
# lst = []
#
# while number != "end":
#     number = input("число: ")
#     if number.lstrip("-").isdigit(): # .lstrip("-") - удалить "-" слева
#         number = int(number)
#         lst.append(number)
#     elif number == "end":
#         break # выход из цикла
#     else:
#         print("число плиз!")
#         continue # перезапускает цикл
#
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# print(lst)
# print(f"chetnie: {chet}sht.")
# print(f"nechetnie: {nechet}sht.")

lst = [-5, -8, 2, 14, 1]
mini = min(lst)
maxi = max(lst)

# lst.index(mini) - индекс значения
# lst[] - само значение

lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)], lst[lst.index(mini)]
print(lst)


