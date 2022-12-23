n = int(input("Nhập n: "))
sum = 0
for i in range(1,n+1):
    sum += 1/(2*n)
print(f"S = {round(sum,2)}")
# S = 1/2 + 1/4 + ... + 1/2n