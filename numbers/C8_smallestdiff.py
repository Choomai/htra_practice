from itertools import combinations

with open("io/C8_smallestdiff.inp") as f:
    N = int(f.readline())
    cards = tuple(map(int, f.readline().split()))

cards_combs = combinations(cards, N//2)
min_diff = float("inf")

for cards1, cards2 in combinations(cards_combs, 2):
    current_diff = abs(sum(cards1) - sum(cards2))
    if current_diff < min_diff:
        min_diff = current_diff
    elif current_diff == 0:
        print(0)
        exit(0)

print(min_diff)