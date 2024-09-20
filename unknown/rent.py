from dataclasses import dataclass
from itertools import combinations

@dataclass
class Customer:
    start_time: int
    end_time: int
    pay: int
    index: int

    def __lt__(self, other: object) -> bool:
        return self.start_time < other.start_time
    def __gt__(self, other: object) -> bool:
        return self.start_time > other.start_time

with open("io/rent.inp", "r") as f:
    N = int(f.readline())
    customers = [Customer(*map(int, f.readline().split()), i) for i in range(N)]

def check(selected: combinations) -> bool:
    if len(selected) == 1: return True

    selected = tuple(sorted(selected))
    for i in range(0, len(selected)-1):
        if selected[i].end_time > selected[i+1].start_time: return False
    return selected

max_income = 0
selected_comb = None
for i in range(N, 1, -1): # N -> 2
    for comb in combinations(customers, i):
        current_income = sum((customer.pay for customer in comb))
        if current_income <= max_income: continue

        passed_comb = check(comb)
        if not passed_comb: continue
        max_income = current_income
        selected_comb = passed_comb

print(len(selected_comb), max_income)
print(*(comb.index+1 for comb in selected_comb))