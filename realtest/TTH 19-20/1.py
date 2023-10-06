import itertools
combs = itertools.product("wb", repeat=int(input()))
for comb in combs: print("".join(comb))