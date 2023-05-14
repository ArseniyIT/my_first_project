a = int(input())
count = 0
for i in range(a):
    b = input()
    if b.count("++"):
        count += 1
    elif a.count("--"):
        count -= 1

print(count)
