# Consider one item at a time, and increase the knapsack capacity from 0 to the knapsack limit.
# If the current item is not too heavy, check what gives the highest value: adding it, or not adding it. Store the maximum of these two values in the table.
# In case the current item is too heavy to be added, just use the previously calculated value at the current capacity where the current item was not considered.

from pprint import pprint

weights, values = [], []
with open("io/BAG.inp", "r") as f:
    N, W = map(int, f.readline().split())
    for _ in range(N):
        weight, value = map(int, f.readline().split())
        weights.append(weight)
        values.append(value)

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, W+1):
        if weights[i-1] > w:
            dp[i][w] = dp[i-1][w]
        else: 
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + values[i-1])
pprint(dp)