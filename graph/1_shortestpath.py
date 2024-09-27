from itertools import permutations, pairwise

with open("io/1_shortestpath.inp", "r") as f:
    N, P = map(int, f.readline().split())
    paths = {}
    for _ in range(P):
        start, end, length = map(int, f.readline().split())
        paths[f"{start}-{end}"] = length
    
def check(path: tuple) -> bool:
    global N
    return path[0] == 0 and path[-1] == N-1

saved_path = None
min_length = float("inf")

for i in range(2, N+1):
    if saved_path: break

    for path in filter(check, permutations(range(N), i)):
        current_length = 0
        for start, end in pairwise(path):
            try: current_length += paths[f"{start}-{end}"]
            except KeyError:
                current_length = None
                break
        if current_length and current_length < min_length:
            min_length = current_length
            saved_path = path

print(min_length)
print(*saved_path, sep=" -> ")