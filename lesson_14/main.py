# множества
# 1) повторения исключеный
# d1 = {"алег", "Антон", "ант"}
# 2) неупорядоченные
# print(d1)
# 3) пустое множество - толкьо set()
# 4) внутри только неизменияемые данные


# словари
# 1) изменяемый тип данных
# anton = ""
# d = {
#     anton: 1,
# }
# print(d)
# 3) пустой словарь = dict() или {}

# первая задача
# phrase = "Маша, Ты Где? мАШа загОРает.".lower() # опустили регистор
# spisok_nechisti = list("!,.?") # строка -> список
# phrase_cleared = ""
# d = {}
#
# for i in phrase: #перебор по символам
#     if i not in spisok_nechisti:
#         phrase_cleared += i
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l: # интегрируется по словам
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)

# второй задача
# s = 0 # будущая сумма
# chek = {
#     "bread": 100,
#     "milk": 150,
#     "cheese": 80,
#     "elka": 2000,
# }
# # for i in chek: перебор по ключам
# for i in chek.values(): #перебор по значениям
#     s += i # считаем чек
# print(s)

# phrase = "Маша, Ты Где? мАШа загОРает.".lower() # опустили регистор
# spisok_nechisti = list("!,.?") # строка -> список
# phrase_cleared = ""
# d = {}
#
# for i in phrase: #перебор по символам
#     if i not in spisok_nechisti:
#         phrase_cleared += i
# print(phrase_cleared)
# l = phrase_cleared.split(" ")
# print(l)
# for bogdan in l: # интегрируется по словам
#     if bogdan not in d:
#         d[bogdan] = 1
#     else:
#         d[bogdan] += 1
# print(d)
#
# maxi = max(d.values())
# for (key, values) in d.items():
#     if values == maxi:
#         print(f"ключ:{key}, значение:{values}")
#     print(values)

#задача четвертый


d = {
    9: 2,
    5: 7,
    3: 4,
    "ключ4": 9,
    "eee": 6,
}
d["eee"], d[3] = d[3], d["eee"]

del d[5]

d["new_key"] = "new_values"
print(d)


