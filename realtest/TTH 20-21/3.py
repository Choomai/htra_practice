from itertools import combinations

N, K = map(int, input().split())
combs = list(combinations(range(1, N+1), K))
print(*combs, sep="\n")
print(len(combs))