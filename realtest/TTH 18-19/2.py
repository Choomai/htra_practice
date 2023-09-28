from itertools import permutations
n = int(input())
segments = range(1, n + 1)
possibles_combs = list(permutations(segments, n))
for comb in possibles_combs:
    print(*comb, end="; ")
print(f"\n{len(possibles_combs)}")