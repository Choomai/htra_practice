import re
N = input()

total = 0
pattern = re.compile("[2357]")
for num in N:
    if re.match(pattern, num): total += int(num)

print(total)