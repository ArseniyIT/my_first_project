# a = [0,4,2,2,2,3,3,1,4,5,3,2,3,1,4,2,3,4,1,4,1,2]
# for i in range(0, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')
# print()
# for i in range(0, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# import random
#
# b = []
# a = [1, 2, 1, 8, 9, 7, 5, 6, 3, 8, 1, 9, 6]
#
# for i in (a):
#     if i in b:
#         print('yes')
#     else:
#         print('no')
#         b.append(i)
from random import randint
print(max([randint(0, 500) for i in range(100)]))
