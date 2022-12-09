m1 = float(input("Nhập tiền tháng trước: "))
m2 = float(input("Nhập tiền tháng này: "))
if m1 in range(1,61): m1 *= 5000
elif m1 in range(61,160): m1 *= 8000
else: m1 *= 10000
if m2 in range(1,61): m2 *= 5000
elif m2 in range(61,160): m2 *= 8000
else: m2 *= 10000
print(f"Tiền điện 2 tháng: {round(m1+m2,2)}")