weights, values = [None], [None] # 1-based indexes
with open("io/BAG.inp", "r") as f:
    N, W = map(int, f.readline().split())
    for _ in range(N):
        tmp = list(map(int, f.readline().split()))
        weights.append(tmp[0])
        values.append(tmp[1])
    del tmp

dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for w in range(1, W+1):
        if weights[i] > w:
            dp[i][w] = dp[i-1][w]
        else: 
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i]] + values[i])
    
print(dp[N][W])

selected_items = []
i, j = N, W
while i > 1 and j > 1:
    if dp[i][j] != dp[i-1][j]:
        selected_items.append(i)
        j -= weights[i-1]
    i -= 1
print(*selected_items)