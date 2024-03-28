import re

with open("inp/print0and1_less.inp", "r") as f:
    n, k = map(int, f.readline().split())
result = []

for i in range(1, 2**n): 
    cur = f"{i:0>{n}b}"
    if len(re.findall("[1]", cur)) == k: result.append(cur)

with open("out/print0and1_less.out", "w") as f:
    f.write(" ".join(result))