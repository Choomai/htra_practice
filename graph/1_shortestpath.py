from itertools import pairwise

with open("io/1_shortestpath.inp", "r") as f:
    N, P = map(int, f.readline().split())
    possible_paths = {}
    for _ in range(P):
        start, end, length = map(int, f.readline().split())
        possible_paths[f"{start}-{end}"] = length

def get_length(path: range) -> int:
    length = 0
    for start, end in pairwise(path):
        if possible_paths[f"{start}-{end}"]: length += possible_paths[f"{start}-{end}"]
    return length

paths = {}
trip_length = get_length(range(N))
trip = list(range(N))
removed = set()

for current in range(0, N+1): # 1->N
    for back in range(current-2, -1, -1): # current->0
        reverse_length = possible_paths.get(f"{back}-{current}")
        if not reverse_length: continue
        if back in removed or current in removed: continue

        current_length = get_length(range(back, current+1))

        if reverse_length <= current_length:
            for node in range(back+1, current):
                trip.remove(node) # Remove all middle nodes
                removed.add(node)
            trip_length -= current_length
            trip_length += reverse_length
    
print(trip_length)
print(*trip, sep=" -> ")