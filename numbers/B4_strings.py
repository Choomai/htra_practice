from itertools import permutations

input_str = input()
seen = set()
for permute in permutations(input_str, len(input_str)):
    str_permute = "".join(permute)
    if str_permute in seen: continue
    seen.add(str_permute)
    print(str_permute)