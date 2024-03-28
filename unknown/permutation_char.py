import sys
sys.path.append("..")
from null_libs import filename
from itertools import permutations

io_name = filename(__file__)

with open(f"inp/{io_name}.inp", "r") as f:
    inp = f.readline()

with open(f"out/{io_name}.out", "w") as f:
    for mut in permutations(inp, len(inp)):
        f.write("".join(map(str, mut)) + "\n")