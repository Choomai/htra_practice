def getInput(): return [int(elem) for elem in input().split()]

n, m = getInput()
students_cls = getInput()
comp_rooms = getInput()
sorted_comp_rooms = sorted(comp_rooms, reverse=True)

found_counter = 0
found_rooms = []
visited = [False for _ in range(n)]

for cls in students_cls:
    max_diff, max_index = float('inf'), -1
    for comp in sorted_comp_rooms:
        if (comp >= cls + 1) and (max_diff > comp - cls - 1):
            start_at = 0
            while start_at < n - 1:
                tmp_index = comp_rooms.index(comp, start_at)
                if visited[tmp_index]: start_at += 1
                else:
                    max_index = tmp_index
                    break
    
    if max_index != -1:
        found_counter += 1
        found_rooms.append(max_index + 1)
        need_remove = comp_rooms[max_index]
        sorted_comp_rooms.remove(need_remove)

print("==================")
print(found_counter)
print(found_rooms)