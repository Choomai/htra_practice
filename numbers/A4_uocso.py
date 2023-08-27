from math import prod
def divsr(inp) -> list:
    count = 0
    for i in range(1,inp+1):
        if inp % i == 0: count += 1
    return count

t = int(input())
nums = []
for _ in range(t): nums.append(prod([int(elem) for elem in input().split()]))

print("\n".join([str(divsr(elem)) for elem in nums]))