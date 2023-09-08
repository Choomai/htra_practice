import sys
sys.path.append("..")
from null_libs import *

n = int(input())
inp = []
for _ in range(n): inp.append(int(input()))

result = []
for num in inp:
    if (2 * num) <= sum(divsr(num)): result.append(str(num))

print(len(result))
print("\n".join(result))