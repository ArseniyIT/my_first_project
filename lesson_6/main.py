# month = input("Введите номер месяца: ")
# if month.isdigit() and int(month) <= 12 and int(month) > 0:
#     month = int(month)
#     if 3 <= month <= 5:
#         print("Весна")
#     elif 6 <= month <= 8:
#         print("Лето")
#     elif 9 <= month <= 11:
#         print("Осень")
#     else:
#         print("Зима")
# else:
#     print("это не месяц или нету такого")
#
# hour = int(input("введи кол-во часов:"))
# minute = int(input("введи кол-во минут:"))
# second = int(input("введи кол-во секунд:"))
#
# if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
#     print("формат правильный ")
#     print(f"{hour}:{minute}:{second}")
# else:
#     print("Ошибка")
#     if hour > 23 or hour < 0:
#         print("часы в формате [0-23]")
#     if minute > 59 or minute < 0:
#         print("минуты в формате [0-59]")
#     if second > 59 or second < 0:
#         print("секунды в формате [0-59]")

count = 0

q1 = input("какого цвета трава?\n"
           "а) голубая, б) коричневая, в) зеленый, г) красная\n"
           "--> ")
if q1 == "в":
    count += 1
    print("правильно + 1 балл")
else:
    print("неправильно, ты не получавешь 1 балл :(")
    print("твой счет:", count)
    quit()
q2 = input("сколько ног у паука?\n"
           "а)шесть, б)Восемь, в)Девять, г)Семь\n"
           "--> ")
if q2 == "б":
    count += 1
    print("правильно + 1 балл")
else:
    print("неправильно, ты не получавешь 1 балл :(")
    print("твой счет:", count)
    quit()
q3 = input("сколько метров может прорыть крот за одну ночь\n"
      "а)150, б)8, в)100, г)76\n"
      "--> ")
if q3 == "г":
    count += 1
    print("правильно + 1 балл")
else:
    print("неправильно, ты не получавешь 1 балл :(")
    print("твой счет:", count)
    quit()