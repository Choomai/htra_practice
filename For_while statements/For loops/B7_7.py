n = int(input("Nhập n: "))
for i in range(1,n,2):
    if n % i == 0: max = i
print(f"Ước lẻ lớn nhất của {n} là {max}.")