import sys
sys.path.append("..")
from null_libs import *
from collections import Counter

n = int(input())
inp, result = [], []
for _ in range(n): inp.append(int(input()))

inp_counter = Counter(inp)
# print(list(inp_counter.items()))
for num, occr in inp_counter.items():
    if occr == 1: result.append(num)
print(result)