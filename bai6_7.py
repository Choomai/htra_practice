ins = []
ins.append(input("Nhập a: "))
ins.append(input("Nhập b: "))
print(f"{ins[0]} là số nhỏ nhất." if min(ins) == ins[0] else f"{ins[1]} là số nhỏ nhất.")