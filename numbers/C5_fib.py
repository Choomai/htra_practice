from functools import lru_cache

a1, a2 = 1, 1

X = int(input())
while a1 < X and a2 <= X:
    a1, a2 = a2, a2+a1
print(a1)