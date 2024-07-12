import sys
sys.path.append("..")
from null_practice.null_libs import *

m = int(input())
ranges = []
result = []
for _ in range(m): ranges.append([int(elem) for elem in input().split()])

for i in range(m):
    cnt = 0
    for num in range(ranges[i][0], ranges[i][1]):
        if not isPrime(num): continue
        else: cnt += 1
    result.append(cnt)

print("\n".join([str(elem) for elem in result]))