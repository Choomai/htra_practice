from itertools import permutations
from copy import deepcopy

N = int(input())
matrix = [list(range(1, N+1)), list(range(N*2, N, -1))]


sum_matrix_0 = sum(matrix[0])
sum_matrix_1 = sum(matrix[1])
# diff_rows = 



for i in range(1, 2**N):
    tmp_matrix = deepcopy(matrix)
    tmp_sum_matrix_0 = sum_matrix_0
    tmp_sum_matrix_1 = sum_matrix_1
    for sw_index, sw in enumerate(map(int, tuple(bin(i)[2:].zfill(N)))):
        if not sw: continue
        
        value_0, value_1 = tmp_matrix[0][sw_index], tmp_matrix[1][sw_index]
        tmp_matrix[0][sw_index], tmp_matrix[1][sw_index] = value_1, value_0

        tmp_sum_matrix_0 -= value_0
        tmp_sum_matrix_0 += value_1

        tmp_sum_matrix_1 -= value_1
        tmp_sum_matrix_1 += value_0
    if tmp_sum_matrix_0 == tmp_sum_matrix_1:
        print(*tmp_matrix[0])
        print(*tmp_matrix[1])
        print(tmp_sum_matrix_0)
        exit(0)

# print("No Solution")