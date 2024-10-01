from itertools import combinations
from dataclasses import dataclass

@dataclass
class Item:
    weight: int
    value: int

with open("io/supermarket.inp", "r") as f:
    N, MAX_WEIGHT = map(int, f.readline().split())
    items = []
    for _ in range(N): items.append(Item(*map(int, f.readline().split())))

max_weight = 0
max_value = 0
quit_signal = False

def get_weight_value(comb: tuple[Item]) -> tuple:
    weight = 0
    value = 0
    for item in comb:
        weight += item.weight
        value += item.value

    return weight, value

for i in range(N, 0, -1): # N->1
    for comb in combinations(items, i):
        weight, value = get_weight_value(comb)
        if weight > MAX_WEIGHT or weight < max_weight or value < max_value: continue

        max_weight = weight
        max_value = value
        quit_signal = True

    if quit_signal:
        print(max_weight, max_value, sep="\n")
        exit(0)