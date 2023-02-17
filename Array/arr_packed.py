fi = [open("./input/0_NUL.txt","r"),open("./input/1_SEQREAL.inp", "r"),open("./input/2_MINMAX.inp", "r"),open("./input/3_TBC.inp", "r"),open("./input/4_POS.inp", "r"),open("./input/5_ARRSORT.inp", "r"),open("./input/6_PRIME.inp", "r"),open("./input/7_PNUMBER.inp", "r"),open("./input/8_BOBASO.inp", "r"),open("./input/9_capso1.inp", "r"),open("./input/10_capso2.inp", "r"),open("./input/11_capso3.inp", "r"),open("./input/12_dprime.inp", "r"),open("./input/13_DOANCON1.inp", "r"),open("./input/14_DOANCON2.inp", "r"),open("./input/15_DOANCON3.inp", "r"),open("./input/16_PHANTICH.inp", "r"),open("./input/17_TANSO.inp", "r"),open("./input/18_CD.inp", "r"),open("./input/19_HOMEWORK.inp", "r"),open("./input/20_COW.inp", "r")]
fo = [open("./output/0_NUL.txt","r"),open("./output/1_SEQREAL.out", "w"),open("./output/2_MINMAX.out", "w"),open("./output/3_TBC.out", "w"),open("./output/4_POS.out", "w"),open("./output/5_ARRSORT.out", "w"),open("./output/6_PRIME.out", "w"),open("./output/7_PNUMBER.out", "w"),open("./output/8_BOBASO.out", "w"),open("./output/9_capso1.out", "w"),open("./output/10_capso2.out", "w"),open("./output/11_capso3.out", "w"),open("./output/12_dprime.out", "w"),open("./output/13_DOANCON1.out", "w"),open("./output/14_DOANCON2.out", "w"),open("./output/15_DOANCON3.out", "w"),open("./output/16_PHANTICH.out", "w"),open("./output/17_TANSO.out", "w"),open("./output/18_CD.out", "w"),open("./output/19_HOMEWORK.out", "w"),open("./output/20_COW.out", "w")]
def FParser(content: str,mode: str):
    if mode == "n_arr":
        tmp = content.split("\n")
        tmp_n = int(tmp[0])
        tmp_lst = [float(elem) for elem in tmp[1].split(" ")]
        return tmp_n,tmp_lst
for el_fi in fi: el_fi.close()
for el_fo in fo: el_fo.close()