inp = 0
while (inp not in range(1,13)):
    inp = int(input("Nhập tháng: "))
month_list = [
    [],
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
for i in range(1,5):
    if inp in month_list[i]:
        print(f"Tháng {inp} nằm trong quý {i}.")
        break