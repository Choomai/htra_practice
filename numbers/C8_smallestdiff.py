with open("io/C8_smallestdiff.inp") as f:
    N = int(f.readline())
    cards = list(map(int, f.readline().split()))

min_diff = float("inf")

cards_sum1, cards_sum2 = 0, 0
cards.sort(reverse=True)
for card in cards:
    if cards_sum1 >= cards_sum2: cards_sum2 += card
    else: cards_sum1 += card

print(abs(cards_sum1 - cards_sum2))