import sys
sys.path.append("..")
from null_practice.null_libs import *
from statistics import mean
from itertools import combinations
fi = [open("./input/0_NUL.txt","r"),open("./input/1_SEQREAL.inp", "r"),open("./input/2_MINMAX.inp", "r"),open("./input/3_TBC.inp", "r"),open("./input/4_POS.inp", "r"),open("./input/5_ARRSORT.inp", "r"),open("./input/6_PRIME.inp", "r"),open("./input/7_PNUMBER.inp", "r"),open("./input/8_BOBASO.inp", "r"),open("./input/9_capso1.inp", "r"),open("./input/10_capso2.inp", "r"),open("./input/11_capso3.inp", "r"),open("./input/12_dprime.inp", "r"),open("./input/13_DOANCON1.inp", "r"),open("./input/14_DOANCON2.inp", "r"),open("./input/15_DOANCON3.inp", "r"),open("./input/16_PHANTICH.inp", "r"),open("./input/17_TANSO.inp", "r"),open("./input/18_CD.inp", "r"),open("./input/19_HOMEWORK.inp", "r"),open("./input/20_COW.inp", "r")]
fo = [open("./output/0_NUL.txt","r"),open("./output/1_SEQREAL.out", "w"),open("./output/2_MINMAX.out", "w"),open("./output/3_TBC.out", "w"),open("./output/4_POS.out", "w"),open("./output/5_ARRSORT.out", "w"),open("./output/6_PRIME.out", "w"),open("./output/7_PNUMBER.out", "w"),open("./output/8_BOBASO.out", "w"),open("./output/9_capso1.out", "w"),open("./output/10_capso2.out", "w"),open("./output/11_capso3.out", "w"),open("./output/12_dprime.out", "w"),open("./output/13_DOANCON1.out", "w"),open("./output/14_DOANCON2.out", "w"),open("./output/15_DOANCON3.out", "w"),open("./output/16_PHANTICH.out", "w"),open("./output/17_TANSO.out", "w"),open("./output/18_CD.out", "w"),open("./output/19_HOMEWORK.out", "w"),open("./output/20_COW.out", "w")]

# Problem 1
n,arr = FParser(fi[1].read(), "n_line")
lst_res = oddNeven(arr)
fo[1].write(f"{sum(arr)} {sum(lst_res[2])} {sum(lst_res[3])} {sum(arr[1::2])} {sum(arr[::2])}")

# Problem 2
n,arr = FParser(fi[2].read(), "n_line")
fo[2].write(f"{max(arr)} {min(arr)}")

# Problem 3
n,arr = FParser(fi[3].read(), "n_line")
avg = mean(arr)
fo[3].write(f"{avg}\n{min(arr, key=lambda elem: abs(avg-elem))}")

# Problem 4
n,x,arr = FParser(fi[4].read(), "nx_line")
lst_res = oddNeven(arr)
fo[4].write(f"{lst_res[2][0]} {lst_res[3][-1]}\n{arr.index(x) + 1} {len(arr) - arr[::-1].index(x)}")

# Problem 5
n,arr = FParser(fi[5].read(), "n_line")
sorted_lst = [str(elem) for elem in sorted(arr)]
fo[5].write(f"{' '.join(sorted_lst)}\n{' '.join(sorted_lst[::-1])}")

# Problem 6
n,arr = FParser(fi[6].read(), "n_line", convFloat=False)
prime_lst = []
for elem in arr:
    if isPrime(elem): prime_lst.append(elem)
fo[6].write(f"{len(prime_lst)} {sum(prime_lst)}")

# Problem 7
n,arr = FParser(fi[7].read(), "n_line", convFloat=False)
lst_6N8 = []
for elem in arr: 
    if all(sub_elem in ["6","8"] for sub_elem in list(str(elem))): lst_6N8.append(elem)
fo[7].write(str(len(lst_6N8)))

# Problem 8
def isTrig(a,b,c):
    if (a+b>c and a+c>b and b+c>a): return True
    return False
n,arr = FParser(fi[8].read(), "n_line", convFloat=False)
max_p,actual_trig = 0,[]
for subset in combinations(arr,3):
    if isTrig(subset[0],subset[1],subset[2]):
        if sum(subset) > max_p: max_p = sum(subset)
        actual_trig.append(subset)
fo[8].write(f"{len(actual_trig)} {max_p}")

# Problem 9
n,x,arr = FParser(fi[9].read(), "nx_line", convFloat=False)
cnt = 0
for i in range(len(arr) - 1):
    if arr[i] + arr[i + 1] == x: cnt += 1
fo[9].write(str(cnt))

# Problem 10
n,x,arr = FParser(fi[10].read(), "nx_line", convFloat=False)
cnt = 0
for subset in combinations(arr,2):
    if sum(subset) == x: cnt += 1
fo[10].write(str(cnt))

# Problem 11 // Need attention
n,arr = FParser(fi[11].read(), "n_line", convFloat=False)
cnt,tmp_prime = 0,0
for subset in combinations(arr,2):
    if isPrime(sum(subset)):
        tmp_prime = sum(subset)
        break
for subset in combinations(arr,2):
    if sum(subset) == tmp_prime: cnt += 1
fo[11].write(str(cnt))

# Problem 12
n,arr = FParser(fi[12].read(), "n_line", convFloat=False)
cnt,prime_lst = 0,[]
for elem in arr:
    # Conv string -> split each char -> conv each char to int
    elem_splited = [int(subelem) for subelem in list(str(elem))]
    if isPrime(elem) and isPrime(sum(elem_splited)):
        cnt += 1
        prime_lst.append(elem)
fo[12].write(str(cnt) + "\n" + " ".join([str(elem) for elem in prime_lst]))

# Problem 13
n,arr = FParser(fi[13].read(), "n_line", convFloat=False)
cnt,max_cnt,last_num = 1,0,arr[0]
for i in range(1,len(arr)):
    if arr[i] >= last_num: cnt += 1
    else: cnt = 1
    if cnt > max_cnt: max_cnt = cnt
    last_num = arr[i]
fo[13].write(str(max_cnt))

# Problem 14
n,arr = FParser(fi[14].read(), "n_line", convFloat=False)
cnt,max_cnt,last_num = 1,0,arr[0]
for i in range(1,len(arr)):
    if ((arr[i] * -1 >= 0) and last_num >= 0) or ((arr[i] * -1 < 0) and last_num < 0): cnt += 1               
    else: cnt = 1
    if cnt > max_cnt: max_cnt = cnt
    last_num = arr[i]
fo[14].write(str(max_cnt))

# Problem 15
n,arr = FParser(fi[15].read(), "n_line", convFloat=False)
sum_arr,tmp_arr = [],[]
for i in range(2,len(arr)):
    for j in range(len(arr) - i + 1): sum_arr.append(arr[j:j + i])
sum_arr = [sum(subset) for subset in sum_arr]
fo[15].write(str(max(sum_arr)))

# Problem 16
n,i,prime_dict = int(fi[16].read()),2,{}
while True:
    while n % i != 0: i += 1
    if i in prime_dict: prime_dict[i] += 1
    else: prime_dict[i] = 1
    n = n // i
    if n == 1: break
for index,val in prime_dict.items(): fo[16].write(str(index) + " " + str(val) + "\n")

# Problem 17
n,arr = FParser(fi[17].read(), "n_line", convFloat=False)
num_dict = dict.fromkeys(sorted(set(arr)), 0)
for elem in arr: num_dict[elem] += 1
for index,val in num_dict.items(): fo[17].write(str(index) + " " + str(val) + "\n")

# Problem 18
n,s,arr = FParser(fi[18].read(), "nx_line", convFloat=False)
safe_lst,max_len,saved_index = [],0,0
for i in range(len(arr),0,-1):
    for elem in combinations(arr, i):
        if (len(elem) > max_len) and sum(elem) <= s: max_len,saved_index = sum(elem), i
fo[18].write(str(saved_index))

# Problem 19
n,s,arr = FParser(fi[19].read(), "nx_line", convFloat=False)
i_end,cnt = len(arr),0
for i in range(i_end):
    for index,elem in enumerate(arr): 
        if s >= elem: 
            s += elem
            arr.pop(index)
            i_end -= 1
            cnt += 1
            break
fo[19].write(str(cnt))

# Problem 20
# Handling file
raw = fi[20].read().split("\n")
ns_raw = raw.pop(0)
n,s = int(ns_raw.split(" ")[0]), int(ns_raw.split(" ")[1])
saved_tuple,arr = None,[int(elem) for elem in raw]
# Calc
for elem in combinations(arr, n):
    if sum(elem) == 100: saved_tuple = elem
fo[20].write("\n".join([str(elem) for elem in saved_tuple]))
# Save changes to all files.
for el_fi in fi: el_fi.close()
for el_fo in fo: el_fo.close()