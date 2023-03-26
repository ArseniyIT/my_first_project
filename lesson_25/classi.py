from random import randint

# x = 100
#
# class Anton:
#     location = "Novosibirsk" # public static
#     # __location = "секрет" #private static
#     def __init__(self, rost=x - 50, ves=2):
#         self.height = rost # public dynamic
#         self.__weight = ves # private dynamic
#         self.otkuda = Anton.location #использование статики
#
#     def __private(self):
#         pass
#
#     def public(self):
#         pass
#
# chelovek = Anton()
# print(chelovek.height, chelovek.weight)


class Human:
    default_name = "Виктор"
    default_age = 15

    def __init__(self, name=default_name, age=default_age):
        self.imya = name
        self.let = age
        self.__dengi = 5_000
        self.__dom = None

    def info(self):
        return f"Имя: {self.imya},Возраст: {self.let},Средства: {self.__dengi},Дом: {self.__dom}"

    def earn_money(self):
       self.__dengi += 152000


    def default_info(self):
        return f"Имя {Human.default_name}, Возраст {Human.default_age}"

    def __make_deal(self, dom):
        if self.__money >= dom.final_price():
            self.__money -= dom.final_price()
            return True
        else:
            return False

    def buy_house(self, dom):
        if self.__make_deal(dom1):
            dom.owner = self.name
            self.__house = dom
            return "Купили. по кайфу"
        else:
            return f"Денег не хватило, нужно еще {dom.final_pricee() - self.__money}"



Oleg = Human("Олег", 28)

print(Oleg.let)


class House:
    def __init__(self, area, price):
        self.__price = price
        self.__area = area
        self.__skidka = randint(5, 25)

    def final_price(self):
        return(self.__price / 100)*self.__skidka

dom1 = House("nov", 155000)
print(dom1.final_price())

