# мутабельность
# мутабельные - изменяемые
# немуталбельные - неизменяемые
# x = "mavavi"
# x[1] = 'o' #так низя
# x = "movavi"




# списки []
# lst = ["one", "two", "popit"]
# lst.append("spiner") #.append() - добавить в список
# lst.pop(0) #.pop() - удалить по индексу
# lst.remove("two") # .remove() - удалить по значению

# lst = [0, 3, 5, -2, 1]
# lst.reverse()
# print(lst)

# lst1 = [0, 1, 2]
# lst2 = [3, 4, 5]
# lst1.extend(lst2) # .extend = расширить
# print(lst1)

# lst = [1, 2]
# lst.insert(1, 1.5) # .insert() - вставить по индексу

# lst = ["123123"]
# lst.clear() # .clear() - отчистка

# lst = [0, 4, 2, -5, 1]
# lst.sort() # .sort() - сортировка
# lst.sort(reverse=True) # reverse=True от меньшего к большемо
# print(lst)

# кортеж

# tup = (1, 2, 3)
# # tup = 1, 2, 3
# # tup = 1,
# print(max(tup))
# print(min(tup))

# list1 = ["a", "b", "c"]
# list2 = ["0", "1", "2"]
# couple = zip()
#
# for bogdan in couple:
#     print(bogdan)

from collections import namedtuple

citizen = namedtuple("житель", "имя возвраст статус")
alex = citizen(имя="Леха Алексеевич",
               возвраст="27",
               статус="хазбик")

print(alex.имя)
print(alex.возвраст)
print(alex.статус)

print(alex)