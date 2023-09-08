import re

n = int(input())
inp = {}
for _ in range(n): inp[input()] = 0

for code in inp.keys():
    inp[code] = len(re.findall("[0-9]", code))
result = dict(sorted(inp.items(), key=lambda item: item[1]))

print("===============")
for code in result.keys(): print(code)