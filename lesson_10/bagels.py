import random
life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life: # то же самое, что и while != 0
    is_guessed = False #отгадано?
    print("=" * 20)

    print("жизни:", life)

    guess = input("предположение")
    if len(guess) != length or guess.isdigit(): # если длина != 3 или не число
        print("число от 100 до 999")