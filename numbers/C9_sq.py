from math import sqrt
from itertools import combinations_with_replacement

def check(inp: int) -> bool:
    return int(sqrt(inp))**2 == inp

N = int(input())
squares = tuple(filter(check, range(1,N)))

i = 2
while N >= 2:
    for comb in combinations_with_replacement(squares, i):
        if sum(comb) == N:
            print(i)
            exit(0)
    i += 1
else: print(N)