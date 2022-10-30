# import random # подтянуть в проект юбиблиотеку
# print(random.randint(0, 100)) # 0 <= x <= 100

# import random as r
# print(r.randint(0, 100))

# from random import randint # подтянуть только randint з random
# print(randint(0, 100))

# from random import  * # импортировать все из и=модуля (ЭТО ПЛОХО)
# print(randint)

# import random as r
# lst = [0, 1, 2, 3, 4, 5]
# print(r.choice(lst)) # random.choice - выбрать одно случайное
# r.shuffle(lst) # random.shuffle - перемешать содержимое
# print(lst)

import turtle
screen = turtle.Screen() # экран
t = turtle.Turtle() # черепашка
t.pensize(9) # размер
t.pencolor("green")
#
# t.forward(150)
# t.right(90) # повернуть напрраво на 90 градусов
# t.forward(150)
# t.rt(90) # rt - right
# t.forward(150)
# t.left(90)
# t.forward(150)
# t.lt(90) # lt - left
t.shape("arrow")
t.begin_fill() # начало закрашивание
t.color("green", "yellow")
t.speed(5) # 1 - едленно 10- очень быстро 0- макс скорость
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400)
t.right(90)
t.forward(200)
t.right(90)
t.end_fill()

t.penup()
t.goto(240, -75)
t.pendown()
t.forward(75)
t.penup()
t.goto(140, -25)
t.pendown()
t.circle(30) # 30 пикселей диаметр
t.penup()
t.goto(180, -160)
t.pendown()
t.write("Movavi", font=("Arial Black", 50, "normal"), align="center")

screen.exitonclick() # выйти по клику
