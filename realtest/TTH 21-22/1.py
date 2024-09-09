from itertools import permutations

permutes = tuple(map(int, input().split()))
p = int(input())

found_permutes = list(permutations(range(1, len(permutes) + 1), len(permutes)))
print(found_permutes.index(permutes) + 1)
print(*found_permutes[p-1])