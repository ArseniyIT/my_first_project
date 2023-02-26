# try:
#     f = open("bbbaaa.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("i chto")


# try:
#     x = int(input("введи число: "))
#     print(10 / x)
# except ValueError:
#     print("chislo pishi abaldui")
# except ZeroDivisionError:
#     print("ne pishi 0")
# else: # когда не было исключений
#     print("nety problem")
# finally:  # в любом случае
#     print("ne xochy")


# x = input("vvedi imya dryga->")
# try:
#     if x == "anton":
#         raise NameError("xaaxaxxaaxax")
# except NameError as abdul:
#     print("не льзя...", abdul)

#
# def sr_ar():
#     s = 0
#     k = 0
#     for i in text:
#         try:
#             s += int(i)
#         except ValueError:
#             print("найдено не число", i)
#         else:
#             k += 1
#
#     # print(s)
#     # print(k)
#     if k == 0:
#         print("числа остсутствуют")
#     return round(s / k, 2)
#
#
# try:
#     f = open("text.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отсутствует или неправильное название")
# text = f.read().split()
# f.close()
#
# print(sr_ar())


#secondз адача
# try:
#     f = open("text.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отстуствует")
# text = f.readlines()
# print(f"Строк: {len(text)}")
#
# full_text = " ".join(text).replace("\n", "")
# print(full_text)
# words = full_text.split()
# print(f"Слов: {len(words)}")
# symbols = full_text.replace(" ", "")
#
#
# print(f"Символов: {len(symbols)}")
#
#
# f.close()


# word = input("какое слово ищем-> ")
# try:
#     f = open("text.txt", "r", encoding="utf-8")
# except FileNotFoundError:
#     print("файл отстуствует или неправильное название")
# text = f.read()
# f.close()
#
# print(text.count(word))



try:
    f = open("text.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("файл отстуствует")
text = f.read()

numbers = text.split()
print(numbers)
p = 1
for i in numbers:
    p *= int(i)
print(p)