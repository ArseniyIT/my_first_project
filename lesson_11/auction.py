import os

total_bets = []
triger = "yes"

while triger == "yes":
    name = input("имя: ")
    bet = int(input("Ставка: "))
    temp_bet = {"name": name, "bet": bet}
    total_bets.append(temp_bet)
    triger = input("yes - okey lets go, no - stop")
    os.system("cls||clear")

winner = {'name': '', "bet": 0}
for i in range(len(total_bets)):
    if total_bets[i]["bet"] > winner['bet']:
        winner["name"] = total_bets[i]['name']
        winner["bet"] = total_bets[i]['bet']

print(f"Победитель: {winner['name']} и его ставка: {winner['bet']}")