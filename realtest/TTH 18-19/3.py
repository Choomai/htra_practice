with open("io/3.inp", "r") as f:
    candy_packs = sorted([int(pack) for pack in f.readline().split()], reverse=True)
group_1, group_2 = [],[]
sum_1, sum_2 = 0,0
for pack in candy_packs:
    if sum_1 < sum_2:
        group_1.append(pack)
        sum_1 += pack
    else:
        group_2.append(pack)
        sum_2 += pack

print(abs(sum_1 - sum_2), group_1, group_2, sep="\n")