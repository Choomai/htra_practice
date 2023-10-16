from pprint import pprint
n, m = [int(elem) for elem in input().split()]
map_2d = [[0 for _ in range(m)] for __ in range(n)]
dd_arr = [] # 2D array
d_arr = [] # 1D for combs()
for _ in range(n):
    row_inp = [int(elem) for elem in input().split()]
    dd_arr.append(row_inp)
    d_arr.extend(filter(lambda x: x != 0, row_inp))
d_arr = sorted(d_arr, reverse=True) # -> [9,8,7,6,5,4...]

group_1, group_2 = [],[]
sum_1, sum_2 = 0,0
for cls in d_arr:
    if sum_1 < sum_2:
        group_1.append(cls)
        sum_1 += cls
    else:
        group_2.append(cls)
        sum_2 += cls
# group_1 -> [9] -> [9]   -> [9,6] -> [9,6,5] -> [9,6,5] -> ...
# group_2 -> [8] -> [8,7] -> [8,7] -> [8,7]   -> [8,7,4] -> ...

for cls in group_2:
    x_pos, y_pos = 0,0
    for i in range(n):
        try: x_pos = dd_arr[i].index(cls)
        except ValueError: pass
        else: 
            y_pos = i
            dd_arr[i][x_pos] = 0
            break
    map_2d[y_pos][x_pos] = 1

pprint(map_2d)
print(sum_1, sum_2)