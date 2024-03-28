from itertools import product

with open("inp/1.inp", "r") as inp: n = int(inp.readline())

combs = product("wb", repeat=n)
with open("out/1.out", "w") as out:
    for comb in combs: out.write("".join(comb) + "\n")