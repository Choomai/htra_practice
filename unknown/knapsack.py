from pprint import pprint

with open("io/knapsack.inp", "r") as f:
    N, max_weight = map(int, f.readline().split())

    dp = [[0] * (max_weight+1)]
    weights = [None]
    values = [None]
    for _ in range(N):
        dp.append([0] * (max_weight+1))
        item = tuple(map(int, f.readline().split()))
        weights.append(item[0])
        values.append(item[1])

for i in range(1, N+1):
    for weight in range(1, max_weight+1):
        if weights[i] > weight:
            dp[i][weight] = dp[i-1][weight]
            continue

        dp[i][weight] = max(values[i] + dp[i-1][weight - weights[i]], dp[i-1][weight])

rows_cursor = max_weight
items_index = []
for i in range(N, 0, -1): # N->1
    if dp[i][rows_cursor] == dp[i-1][rows_cursor]: # Item not inclued, so the value stay the same
        continue
    else:
        rows_cursor -= weights[i]
        items_index.append(i)

print(dp[N][max_weight])
print(sorted(items_index))