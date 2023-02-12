import easygui
import random.

def rock_paper_scissors():
    k="пнг картинка/kamen.png"
    b="пнг картинка/bymaga.png"
    n="пнг картинка/nozh.png"
    user=easygui.buttonbox(
        images=[k, b, n],
        choices=("exit",),
    )
    bot=random.choice([k, b, n])

    if user == b and bot == b:easygui.msgbox(msg="ничя")
    elif user == b and bot == k:easygui.msgbox(msg="ти выграл, не играй на наге")
    elif user == b and bot == n:easygui.msgbox(msg="компутер вин")
    elif user == k and bot == n:easygui.msgbox(msg="ю вин")
    elif user == k and bot == k:easygui.msgbox(msg="ничя")
    elif user == k and bot == b:easygui.msgbox(msg="компутер вин")
    elif user == n and bot == n:easygui.msgbox(msg="ничя")
    elif user == n and bot == b:easygui.msgbox(msg="вин")
    else: easygui.msgbox(msg="компутер вин ливай")

    print(user,bot)


def guess_the_number():
    chislo = random.randint(1,100)
    gn = easygui.integerbox(upperbound=100, lowerbound=1, msg="угадай число от 1 до 100")
    while gn != chislo:
        if gn > chislo:
            gn = easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нужно число меньше чем {gn}", image="пнг картинка/l.png")
        elif gn < chislo:
            gn = easygui.integerbox(upperbound=100, lowerbound=1, msg=f"нет, нужно число больше чем {gn}", image="пнг картинка/r.png")
        else:
            gn = easygui.msgbox(msg="win",image="пнг картинка/kamen.png")
games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = easygui.buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()