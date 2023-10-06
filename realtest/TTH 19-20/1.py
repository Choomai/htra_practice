from itertools import product
combs = product("wb", repeat=int(input()))
for comb in combs: print("".join(comb))