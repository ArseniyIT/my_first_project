input()
color = list(input())
ah = 0
del_count = 0
while ah != len(color)-1:
    if color[ah] == color[ah+1]:
        color.pop(ah)
        del_count += 1
    else:
        ah += 1
print(del_count)