from statistics import mean
fi = [open("./input/0_NUL.txt","r"),open("./input/1_SEQREAL.inp", "r"),open("./input/2_MINMAX.inp", "r"),open("./input/3_TBC.inp", "r"),open("./input/4_POS.inp", "r"),open("./input/5_ARRSORT.inp", "r"),open("./input/6_PRIME.inp", "r"),open("./input/7_PNUMBER.inp", "r"),open("./input/8_BOBASO.inp", "r"),open("./input/9_capso1.inp", "r"),open("./input/10_capso2.inp", "r"),open("./input/11_capso3.inp", "r"),open("./input/12_dprime.inp", "r"),open("./input/13_DOANCON1.inp", "r"),open("./input/14_DOANCON2.inp", "r"),open("./input/15_DOANCON3.inp", "r"),open("./input/16_PHANTICH.inp", "r"),open("./input/17_TANSO.inp", "r"),open("./input/18_CD.inp", "r"),open("./input/19_HOMEWORK.inp", "r"),open("./input/20_COW.inp", "r")]
fo = [open("./output/0_NUL.txt","r"),open("./output/1_SEQREAL.out", "w"),open("./output/2_MINMAX.out", "w"),open("./output/3_TBC.out", "w"),open("./output/4_POS.out", "w"),open("./output/5_ARRSORT.out", "w"),open("./output/6_PRIME.out", "w"),open("./output/7_PNUMBER.out", "w"),open("./output/8_BOBASO.out", "w"),open("./output/9_capso1.out", "w"),open("./output/10_capso2.out", "w"),open("./output/11_capso3.out", "w"),open("./output/12_dprime.out", "w"),open("./output/13_DOANCON1.out", "w"),open("./output/14_DOANCON2.out", "w"),open("./output/15_DOANCON3.out", "w"),open("./output/16_PHANTICH.out", "w"),open("./output/17_TANSO.out", "w"),open("./output/18_CD.out", "w"),open("./output/19_HOMEWORK.out", "w"),open("./output/20_COW.out", "w")]
def FParser(content: str,mode: str, convFloat=True):
    tmp = content.split("\n")
    if convFloat: tmp_lst = [float(elem) for elem in tmp[1].split(" ")]
    else: tmp_lst = [int(elem) for elem in tmp[1].split(" ")]
    if mode == "n_arr":
        tmp_n = int(tmp[0])
        return tmp_n,tmp_lst
    if mode == "nx_arr":
        nx_lst = tmp[0].split(" ")
        tmp_n = int(nx_lst[0])
        tmp_x = float(nx_lst[1])
        return tmp_n,tmp_x,tmp_lst
def isPrime(inp: int) -> bool:
    for i in range(2, inp):
        if inp % i == 0: return False
    if inp != 1: return True
    else: return False
def oddNeven(inp: list) -> list:
    odd,even,neg,pos = [],[],[],[]
    for elem in inp:
        if elem % 2 == 0: even.append(elem)
        else: odd.append(elem)
        if elem >= 0: pos.append(elem)
        else: neg.append(elem)
    return [odd,even,neg,pos]

# Problem 1
n,arr = FParser(fi[1].read(), "n_arr")
lst_res = oddNeven(arr)
fo[1].write(f"{sum(arr)} {sum(lst_res[2])} {sum(lst_res[3])} {sum(arr[1::2])} {sum(arr[::2])}")

# Problem 2
n,arr = FParser(fi[2].read(), "n_arr")
fo[2].write(f"{max(arr)} {min(arr)}")

# Problem 3
n,arr = FParser(fi[3].read(), "n_arr")
avg = mean(arr)
fo[3].write(f"{avg}\n{min(arr, key=lambda elem: abs(avg-elem))}")

# Problem 4
n,x,arr = FParser(fi[4].read(), "nx_arr")
lst_res = oddNeven(arr)
fo[4].write(f"{lst_res[2][0]} {lst_res[3][-1]}\n{arr.index(x) + 1} {len(arr) - arr[::-1].index(x)}")

# Problem 5
n,arr = FParser(fi[5].read(), "n_arr")
sorted_lst = [str(elem) for elem in sorted(arr)]
fo[5].write(f"{' '.join(sorted_lst)}\n{' '.join(sorted_lst[::-1])}")

# Problem 6
n,arr = FParser(fi[6].read(), "n_arr", convFloat=False)
prime_lst = []
for elem in arr:
    if isPrime(elem): prime_lst.append(elem)
print(prime_lst)
fo[6].write(f"{len(prime_lst)} {sum(prime_lst)}")
for el_fi in fi: el_fi.close()
for el_fo in fo: el_fo.close()