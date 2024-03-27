from itertools import permutations

n = int(input())
for mut in permutations(range(n), n):
    print("".join(map(str, mut)), end=" ")