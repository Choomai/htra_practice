fi = [open("./input/0_NUL.txt", "r"),open("./input/1_PRIMECNT.inp", "r"),open("./input/2_SothuK.inp", "r"),open("./input/3_Xauthuannhat.inp", "r"),open("./input/4_Toigian.inp", "r"),open("./input/5_Special.inp", "r")]
fo = [open("./output/0_NUL.txt", "r"),open("./output/1_PRIMECNT.out", "w"),open("./output/2_SothuK.out", "w"),open("./output/3_Xauthuannhat.out", "w"),open("./output/4_Toigian.out", "w"),open("./output/5_Special.out", "w")]
import sys
sys.path.append("..")
from null_libs import *
from collections import Counter
from fractions import Fraction

# Problem 1
n, mixed_arr = FParser(fi[1].read(), "n_arr", convFloat=False)
for sub_arr in mixed_arr:
    cnt = 0
    for i in range(sub_arr[0] if sub_arr[0] < sub_arr[1] else sub_arr[1], sub_arr[1] if sub_arr[1] > sub_arr[0] else sub_arr[0]):
        if isPrime(i): cnt += 1
    fo[1].write(str(cnt) + "\n")

# Problem 2
# I hate algorithm...
# Example: num_digits = 2, k = 13
# Check if k is larger than total length of numbers that are 2 digits long
# 9 * 10^1 is find total numbers that are 2 digits long.
# Multiply it by 2 result in the total length of these numbers.
# To find the number, get the smallest number that are 2 digits long
# + index left after subtract length of these number that are 1 digit long, div it by 2 = 1
# 10 + 1 = 11
k = int(fi[2].read())
num_digits = 1
while k > 9 * (10 ** (num_digits - 1)) * num_digits:
    k -= 9 * (10 ** (num_digits - 1)) * num_digits
    num_digits += 1
num = 10 ** (num_digits - 1) + (k - 1) // num_digits
fo[2].write(str(num)[(k - 1) % num_digits])

# Problem 3
un_encoded, un_decoded = fi[3].read().split("\n")
fo[3].write("".join(Counter(un_encoded).elements()) + "\n" + deCounter(un_decoded))

# Problem 4
splited = fi[4].read().split("\n")
frac = [int(elem) for elem in splited[0].split()] + [int(elem) for elem in splited[1].split()]
frac_obj = Fraction(frac[0], frac[1]) + Fraction(frac[2], frac[3])
fo[4].write(str(frac_obj.numerator) + " " + str(frac_obj.denominator))

# Problem 5
splited = fi[5].read().split("\n")
counter_obj = Counter(splited)
fo[5].write(list(filter(lambda key: counter_obj[key] == 1, counter_obj.keys()))[0])

# Save changes to all files.
for el_fi in fi: el_fi.close()
for el_fo in fo: el_fo.close()