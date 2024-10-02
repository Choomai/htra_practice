from dataclasses import dataclass

@dataclass
class Guest:
    start: int
    end: int
    profit: int
    index: int
    
    def __lt__(self, other: object) -> bool:
        return self.end < other.end
    def __gt__(self, other: object) -> bool:
        return self.end > other.end

with open("io/internetcafe.inp", "r") as f:
    N = int(f.readline())
    guests = [Guest(0,0,0,0)]
    for i in range(N):
        guests.append(Guest(*map(int, f.readline().split()), i+1))

guests.sort()
dp = [0] * (N+1)
indexes = [-1] * (N+1)

for i in range(1, N+1):
    for j in range(i):
        if guests[j].end >= guests[i].start: continue

        if guests[j].profit + guests[i].profit > dp[i]: # Include the guest
            dp[i] = guests[j].profit + guests[i].profit
            indexes[i] = j

current_index = [i for i in range(N+1) if indexes[i] > 0]

max_income, max_income_index = 0, 0
for index, income in enumerate(dp):
    if income > max_income:
        max_income = income
        max_income_index = index

found_indexes = []
while max_income_index > 0:
    found_indexes.append(guests[max_income_index].index)
    max_income_index = indexes[max_income_index]

print(len(found_indexes), max_income)
print(*sorted(found_indexes))