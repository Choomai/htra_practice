from itertools import permutations

mut_inp = input().split()
id = int(input())
n = len(mut_inp)

permutations_list = list(map(lambda mut: "".join(map(str, mut)), permutations(range(n), n)))
print(permutations_list)