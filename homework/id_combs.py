from itertools import combinations

n, k = map(int, input().split())
combs = list(map(
    lambda comb: "".join(map(str, comb)),
    combinations(range(1, n+1), k)
))

id = int(input())
comb_inp = "".join(input().split())
print(f"{'':#>10}")
print(combs[id-1])
print(combs.index(comb_inp) + 1)