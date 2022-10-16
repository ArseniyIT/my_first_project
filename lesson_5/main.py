# x = 7
#
# if x < 10: # больше либо равно
#     print("Я сработал!")
# else:
#     print("Ну я тоже сработав")
#
# phrase = "я карта"
# if phrase == "ya karta":
#     print("Мы карты!")
#
# game = "dota2"
# if game != "brawl stars":
#     print("Ну можно и поиграть")
#
# x = 7
#
# if x >= 10 and (x == 0 or x ==666):
#     print("я не выполню хоть и ошибок нет")
# else:
#     print("ну я тоже сработав")
#
# number = int(input("Введите число: "))
# if number > 0:
#     print("положительное")
# elif number == 0:
#     print("Нулик")
# else: print("отрицательное")
#
# year = int(input("Введите где: "))
# if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
#     print("високосененько")
# else:
#     print("не високосненько")
#
# number_1 = int(input("первое число надо: "))
# operation = input("введите операцию(-,+,*,/):").strip()
# number_2 = int(input("секонд число надо: "))
# lst = ["-", "+", "*", "/"] # список допустимых опираций
# if operation in lst:
#     if operation == "-":
#         print(number_1 - number_2)
#     elif operation == "+":
#         print(number_1 + number_2)
#     elif operation == "*":
#         print(number_1 * number_2)
#     elif operation == "/":
#         print(number_1 / number_2)
#
# number_1 = int(input("ферст число: "))
# number_2 = int(input("секонд число: "))
# number_3 = int(input("треьте число: "))
#
# counter_pol = 0 # счетчик положительных
# counter_otr = 0 # счетчик отрицательных
#
# if number_1 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
#
# if number_2 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
#
# if number_3 < 0:
#     counter_otr += 1 # прибавить к отрицательным
# else:
#     counter_pol += 1 # прибавить к положительным
#
# print("положительных", counter_pol)
# print("отрицательное", counter_otr)
#
# number_1 = int(input("ферст число: "))
# number_2 = int(input("секонд число: "))
# number_3 = int(input("треьте число: "))
#
# lst = [number_1, number_2, number_3]
#
# maxi = max(lst)
# mini = min(lst)
# print("минимальное:", mini)
# print("максимальное:", maxi)

ticket = input("введите номер биета(6 знаков): ")
if len(ticket) == 6 and ticket.isdigit():
    first_half = ticket[0:3]
    second_half = ticket[-3:]

    first_sum = first_half[0] + first_half[1] + first_half[2]
    last_sum = second_half[0] + second_half[1] + second_half[2]

    if first_sum == last_sum:
        print("счастливый билет")
    else:
        print("ну, не повезло")
else:
    print("введи нормально, аа паже")

