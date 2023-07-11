t = int(input())
nums, result = [], []
for _ in range(t): nums.append([int(elem) for elem in input().split()])

for arr in nums:
    small = arr[0] * arr[1]
    org_n = arr[4] # Backup N
    for a in range(arr[0], arr[0] - arr[4]-1, -1): # A to A-N, go down.
        if a < arr[2]: break
        arr[4] = org_n - (arr[0] - a)
        for b in range(arr[1], arr[1] - arr[4]-1, -1): # B-N to B, go down
            if b < arr[3]: break
            small = min(a * b, small)
    print(small)