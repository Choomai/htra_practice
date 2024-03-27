from itertools import permutations

n, k = map(int, input().split())
result = []
for comb in permutations(range(1, n+1), k):
    result.append("".join(map(str, comb)))

print(result)