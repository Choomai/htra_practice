from itertools import permutations

n = int(input())
for mut in permutations(range(1, n+1), n):
    print("".join(map(str, mut)), end=" ")