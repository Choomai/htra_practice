ins = []
for i in range(0,3):
    tmp_inp = float(input(f"Nhập cạnh thứ {i+1}: "))
    ins.append(tmp_inp)
# End inp
res = bool(ins[0]+ins[1]>ins[2] and ins[0]+ins[2]>ins[1] and ins[1]+ins[2]>ins[0])
print("Là tam giác" if res else "Không phải tam giác.")