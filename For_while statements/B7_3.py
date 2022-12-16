n = int(input("Nhập n: "))
sum = 1
for i in range(2,n+1):
    sum += 1/n
print(f"S = {round(sum,2)}")
# S = 1 + 1/2 + 1/3 + ... + 1/n