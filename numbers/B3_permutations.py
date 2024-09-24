from itertools import permutations

with open("io/B3_permutations.inp", "r") as f:
    n = int(f.readline())
    input_permute = tuple(map(int, f.readline().split()))

permutes = tuple(permutations(range(1, n+1), n))

quit_signal = False
for permute in permutes:
    if quit_signal:
        print(permute)
        exit(0)
    if permute == input_permute:
        quit_signal = True
        continue

if quit_signal: print(permutes[0])