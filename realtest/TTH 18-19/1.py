n, m = [int(elem) for elem in input().split()]
distances = [int(elem) for elem in input().split()]
consume_rates = [int(elem) for elem in input().split()]
sorted_dist = sorted(distances, reverse=True)
sorted_csm_rt = sorted(consume_rates)

def calc(dist_arr: list, csm_arr: list) -> list:
    result, indexes = 0, []
    for index in range(len(dist_arr)): # or csm_arr
        tmp = dist_arr[index] * csm_arr[index]
        result += tmp
        indexes.insert(distances.index(dist_arr[index]), str(consume_rates.index(csm_arr[index]) + 1))
        # Insert the current distance and current fuel consumption
        # to location matching the index at un-sorted distance
    
    return result, indexes

if len(distances) == len(consume_rates):
    print(calc(sorted_dist, sorted_csm_rt))
    exit(0)

for _ in range(m - n): sorted_csm_rt.pop()
final_result, indexes = calc(sorted_dist, sorted_csm_rt)
print(final_result)
print("\n".join(indexes))