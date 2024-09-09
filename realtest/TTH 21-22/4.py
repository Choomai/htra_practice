from itertools import permutations

routes = {} # start_id, end_id, length
with open("io/CAR.inp", "r") as f:
    n, m = map(int, f.readline().split())
    for _ in range(m):
        start_id, end_id, length = map(int, f.readline().split())
        routes[f"{start_id}-{end_id}"] = length

def calc(route: list) -> int:
    total = 0
    for i in range(len(route) - 1):
        index = f"{route[i]}-{route[i+1]}"
        if not routes.get(index): index = f"{route[i+1]}-{route[i]}"
        total += routes.get(index)
    return total
    
min_length = float('inf')
saved_route = None
possible_paths = permutations(range(2, n+1), n-1)
for path in possible_paths:
    current_path = [1, *path, 1]
    found_length = calc(current_path)
    if found_length < min_length:
        saved_route = current_path
        min_length = found_length

print(saved_route, min_length, sep="\n")