from random import randint
ins = []
res = True
for i in range(0,3):
    tmp_inp = float(input(f"Nhập cạnh thứ {i+1}: "))
    ins.append(tmp_inp)
tmp_chk = ins[randint(0,2)]
for i in range(0,3):
    if (ins[i] != tmp_chk): res = False
print("Là tam giác đều." if res else "Không phải tam giác đều.")