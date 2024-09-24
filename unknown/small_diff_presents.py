from itertools import combinations

with open("io/presents.inp", "r") as f:
    n,k = map(int, f.readline().split())
    presents = list(map(int, f.readline().split()))

presents.sort(reverse=True)
selection = [None, None]

def check(presents: list) -> bool:
    for comb in combinations(presents, 2):
        if abs(comb[0] - comb[1]) > k: return False
    return True

for sel_index in range(2):
    presents_count = 2
    current_selection = [presents.pop(0)]
    while presents_count <= n // 2:
        for i in range(1, presents_count):
            if presents[0] - current_selection[-1] > k: break
            else: 
                current_selection.append(presents.pop(0))
        presents_count += 1
    selection[sel_index] = current_selection
        

print(selection)