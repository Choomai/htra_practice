n = int(input("Nhập n: "))
sum = 0
for i in range(1,n+1):
    sum += 1/(2*i+1)
    print(2*i+1)
print(f"S = {round(sum,2)}")
# S = 1/3 + 1/5 + ... + 1/2n+1