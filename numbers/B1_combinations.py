from itertools import combinations

with open("io/B1_combinations.inp", "r") as f:
    n,k = map(int, f.readline().split())
    input_comb = tuple(map(int, f.readline().split()))

combs = tuple(combinations(range(1, n+1), k))
quit_signal = False
for comb in combs:
    if quit_signal:
        print(*comb)
        exit(0)
    if comb == input_comb: 
        quit_signal = True
        continue

if quit_signal: print(*combs[0])