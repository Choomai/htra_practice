from itertools import permutations

mut_inp = "".join(input().split())
id = int(input())
n = len(mut_inp)

permutations_list = list(map(
    lambda mut: "".join(map(str, mut)), # Convert (3,2,1) to "321"
    permutations(range(1, n+1), n)
))

print(permutations_list.index(mut_inp) + 1)
print(permutations_list[id+1])