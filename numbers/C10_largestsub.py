with open("io/C79_sum.inp", "r") as f:
    N = int(f.readline())
    inp_arr = list(map(int, f.readline().split()))

saved_sub = None
total = -float("inf")

for i in range(1, N+1):
    for j in range(N+1-i):
        current_sub = inp_arr[j:j+i]
        current_total = sum(current_sub)
        if current_total > total:
            total = current_total
            saved_sub = current_sub


print(total)
print(*saved_sub)