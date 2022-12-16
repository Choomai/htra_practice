inp = 0
while (inp not in range(1,12)):
    inp = int(input("Nhập tháng: "))
if inp in [1,3,5,7,8,10,12]: print(f"Tháng {inp} có 31 ngày.")
elif inp in [4,6,9,11]: print(f"Tháng {inp} có 30 ngày.")
else:
    year = int(input("Nhập năm: "))
    if year % 4 == 0: print(f"Tháng {inp} có 29 ngày.")
    else: print(f"Tháng {inp} có 28 ngày.")