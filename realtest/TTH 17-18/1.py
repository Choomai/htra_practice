from itertools import permutations
import re


n = int(input())
bricks_arr = []
for _ in range(n): bricks_arr.append(input())
possible_solutions = permutations(bricks_arr, n)

result = 0

for solution in possible_solutions:
    solution_str = re.findall(r"[0-9]+", "".join(solution))
    found_str = max(solution_str, key=len)
    found_sum = sum([int(num) for num in list(found_str)])
    if found_sum > result: result = found_sum

print(result)