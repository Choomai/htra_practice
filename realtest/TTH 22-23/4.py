from itertools import combinations
from string import ascii_lowercase

t = int(input())
grp_work = []
for _ in range(t): grp_work.append([int(elem) for elem in input().split()])

for k, n in grp_work: print(len(list(combinations(ascii_lowercase[:k], n))))
