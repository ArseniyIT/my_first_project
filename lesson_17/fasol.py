def beans(x:int): # отнимание фасоли
    global fassol
    fassol -= x



fassol = 20
while True:
    # hod pervogo igroka
    while True:# проверка корекности
        first = int(input("perviy igrok: 1,2 ili 3 boba"))
        if first <= 3 and first >= 1:
            break
    beans(first)
    if fassol < 1:
        print("vtoroi win")
        break
    elif fassol == 1:
        print("perviy win")
    print(fassol)

    # hod vtorogo igroka
    while True:  # проверка корекности
        second = int(input("vtoroi igrok: 1,2 ili 3 boba"))
        if second <= 3 and second >= 1:
            break
    beans(second)
    if fassol < 1:
        print("perviy win")
        break
    elif fassol == 1:
        print("vtoroi win")
    print(fassol)
