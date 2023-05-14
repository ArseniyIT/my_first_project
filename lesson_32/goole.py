f = int(input())
u = 0
for i in range(f):
    a = input()
    p = a.split()
    if int(p[0]) + int(p[1]) + int(p[2]) >= 2:
        u += 1
print(u)
