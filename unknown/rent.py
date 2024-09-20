from dataclasses import dataclass
from itertools import combinations

@dataclass
class Customer:
    start_time: int
    end_time: int
    pay: int
    index: int

with open("io/rent.inp", "r") as f:
    N = int(f.readline())
    customers = [Customer(*map(int, f.readline().split()), i) for i in range(N)]

# def check(selected: combinations) -> bool:
#     if len(selected) == 1: return True

#     selected = list(selected)
#     selected.sort(key=lambda x: x.start_time)

#     for i in range(0, len(selected)-1):
#         if selected[i].end_time > selected[i+1].start_time: return False
#     return selected

# max_income = 0
# selected_comb = None
# for i in range(N, 1, -1): # N -> 2
#     for comb in combinations(customers, i):
#         current_income = sum((customer.pay for customer in comb))
#         if current_income <= max_income: continue

#         passed_comb = check(comb)
#         if not passed_comb: continue
#         max_income = current_income
#         selected_comb = passed_comb


# print(len(selected_comb), max_income)
# print(*(comb.index+1 for comb in selected_comb))

customers.sort(key=lambda x: x.start_time)
dp = [{"income": 0, "indexes": []} for _ in range(N+1)]

for i in range(1, N+1):
    j = 0
    while j < i and customers[j].end_time <= customers[i-1].start_time: j += 1

    if dp[i-1]["income"] > dp[j]["income"] + customers[i-1].pay:
        dp[i]["income"] = dp[i-1]["income"]
        dp[i]["indexes"] = dp[i-1]["indexes"]
    else:
        dp[i]["income"] = dp[j]["income"] + customers[i-1].pay
        dp[i]["indexes"] = dp[j]["indexes"] + [customers[i-1].index + 1]

print(dp[-1]["income"])
print(*dp[-1]["indexes"])