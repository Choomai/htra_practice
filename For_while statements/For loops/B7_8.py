a = int(input("Nhập a: "))
n = int(input("Nhập n: "))
res = 1
for i in range(1,n+1):
    res *= a
print(f"a^n = {res}")
# print(f"a^n = {a**n}")