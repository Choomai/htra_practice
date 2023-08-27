t = int(input())
nums = []
for _ in range(t): nums.append([int(elem) for elem in input().split()])

for arr in nums:
    A, B, X, Y, N = arr
    min_product = float('inf') # Get an infinity float number.
    for a_used in [0, N]:
        b_used = min(N - a_used, B - Y)
        a = max(A - (N - b_used), X)
        b = B - b_used
        min_product = min(min_product, a * b)
        A, B, X, Y = B, A, Y, X
    print(min_product)