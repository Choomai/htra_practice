from itertools import combinations

n, k = map(int, input().split())
for comb in combinations(range(1, n+1), k):
    print("".join(map(str, comb)), end=" ")