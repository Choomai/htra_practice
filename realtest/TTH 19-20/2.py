from pprint import pprint
n, m = [int(elem) for elem in input().split()]
map_2d = [[0 for _ in range(m)] for __ in range(n)]
dd_arr = [] # 2D array
d_arr = [] # 1D for combs()
for _ in range(n):
    row_inp = [int(elem) for elem in input().split()]
    dd_arr.append(row_inp)
    d_arr.extend(filter(lambda x: x != 0, row_inp))
d_arr = sorted(d_arr, reverse=True)

group_1, group_2 = [],[]
sum_1, sum_2 = 0,0
for cls in d_arr:
    if sum_1 < sum_2:
        group_1.append(cls)
        sum_1 += cls
    else:
        group_2.append(cls)
        sum_2 += cls

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