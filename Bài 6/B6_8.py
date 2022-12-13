m1 = float(input("Nhập chữ tháng trước: "))
m2 = float(input("Nhập chữ tháng này: "))
sub = m1-m2
if sub in range(1,61): sub *= 5000
elif sub in range(61,160): sub *= 8000
else: sub *= 10000
print(f"Tiền điện 2 tháng: {round(sub,2)}")