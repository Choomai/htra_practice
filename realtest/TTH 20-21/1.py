# Consider one item at a time, and increase the knapsack capacity from 0 to the knapsack limit.
# If the current item is not too heavy, check what gives the highest value: adding it, or not adding it. Store the maximum of these two values in the table.
# In case the current item is too heavy to be added, just use the previously calculated value at the current capacity where the current item was not considered.

weights, values = [], []
with open("realtest/TTH 20-21/io/BAG.inp", "r") as f:
    N, W = map(int, f.readline().split())
    for _ in range(N):
        weight, value = map(int, f.readline().split())
        weights.append(weight)
        values.append(value)

dp = (N + 1) * [(W + 1) * [0]] # 2D array, N+1 columns, W+1 rows, 0 filled