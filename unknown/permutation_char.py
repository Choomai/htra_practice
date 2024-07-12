from itertools import permutations


with open(f"io/permutation_char.inp", "r") as f:
    inp = f.readline()

with open(f"io/permutation_char.out", "w") as f:
    for mut in permutations(inp, len(inp)):
        f.write("".join(map(str, mut)) + "\n")