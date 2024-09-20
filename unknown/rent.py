from dataclasses import dataclass

@dataclass
class Customer:
    start_time: int
    end_time: int
    pay: int
    index: int

with open("io/rent.inp", "r") as f:
    N = int(f.readline())
    customers = [Customer(*map(int, f.readline().split()), i) for i in range(N)]

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