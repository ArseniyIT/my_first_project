from classi import Human, House
import easygui

easygui.enterbox(msg="как твое имя")
easygui.enterbox(msg="сколько тебе лет")

chelovek = Human(imya, age)
dom1 = House()
dom15 = House()

print(chelovek.buy_house(dom1))
print(chelovek.buy_house(dom1))