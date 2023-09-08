n = int(input())
inp = [int(elem) for elem in input().split()]
max_val = 0

for i in range(n-1):
    current = inp[i] + inp[i+1]
    if current > max_val: max_val = current

print(max_val)