from itertools import combinations_with_replacement

with open("io/PETROL.inp", "r") as f:
    n, k = map(int, f.readline().split())
    tanks = tuple(map(int, f.readline().split()))

i = 2
while n >= 2:
    for comb in combinations_with_replacement(tanks, i):
        if sum(comb) == k:
            print(len(comb))
            print(comb)
            exit(0)
    i += 1

if n == 1: print(k // tanks[0])