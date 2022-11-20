import random
life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life: # то же самое, что и while != 0
    is_guessed = False #отгадано?
    print("=" * 20)

    print("жизни:", end="")
    for _ in range(life):
        print("❤", end="")
    print()

    guess = input("предположение: ")
    if len(guess) != length or not guess.isdigit(): # если длина != 3 или не число
        print("число от 100 до 999")
        continue

    # проверка
    if guess == answer:
        print("победа 🥇")
        is_guessed = True
        break

    if is_guessed == False:
        #проверка на fermi
        for i in range(length):
            if guess[i] == answer[i]:
                print("fermi")
                is_guessed = True
                break #выход из цикла

    if is_guessed == False:
        # проверка на pico
        for char in guess:
            if char in answer:
                print("Pico")
                is_guessed = True
                break

    if is_guessed == False:
        print("Bagels")
    life -= 1