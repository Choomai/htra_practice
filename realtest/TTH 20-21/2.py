with open("io/LETTER.inp", "r") as f:
    n, k = map(int, f.readline().split())
    building_dists = []
    for _ in range(n):
        building_dists.append(list(map(int, f.readline().split())))
    
bins = set()
def max_dists(index: int, max_dist: int):
    if index == n: return max_dist
    if len(bins) == k: return max_dist
    global building_dists

    curr_max = max(building_dists[index][bin] for bin in bins) if bins else 0
    
    bins.add(index)
    max_dist_add = max_dists(index+1, max(curr_max, max_dist))
    bins.remove(index)
    max_dist_rm = max_dists(index+1, max_dist)

    return min(max_dist_add, max_dist_rm)

print(max_dists(0, 0))
print(*bins)