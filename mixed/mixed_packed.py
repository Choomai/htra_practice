fi = [open("./input/0_NUL.txt", "r"),open("./input/1_PRIMECNT.inp", "r"),open("./input/2_SothuK.inp", "r"),open("./input/3_Xauthuannhat.inp", "r"),open("./input/4_Toigian.inp", "r"),open("./input/5_Special.inp", "r")]
fo = [open("./output/0_NUL.txt", "r"),open("./output/1_PRIMECNT.out", "w"),open("./output/2_SothuK.out", "w"),open("./output/3_Xauthuannhat.out", "w"),open("./output/4_Toigian.out", "w"),open("./output/5_Special.out", "w")]
import sys
sys.path.append("..")
from null_libs import *

# Save changes to all files.
for el_fi in fi: el_fi.close()
for el_fo in fo: el_fo.close()