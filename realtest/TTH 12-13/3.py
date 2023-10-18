def getInput(): return [int(elem) for elem in input().split()]

n, m = getInput()
students_cls = getInput()
comp_rooms = getInput()
sorted_comp_rooms = sorted(comp_rooms, reverse=True)

found_counter = 0
found_rooms = []
visited = [False for _ in range(m)]

for cls in students_cls:
    cls_found = False
    for comp in sorted_comp_rooms:
        max_diff, max_index = float('inf'), -1
        if (comp >= cls + 1) and (max_diff > comp - cls - 1):
            start_at = 0
            while start_at < n:
                tmp_index = comp_rooms.index(comp, start_at)
                if visited[tmp_index]: start_at += 1
                else:
                    max_index = tmp_index
                    visited[tmp_index] = True
                    break
    
        if max_index != -1:
            found_counter += 1
            found_rooms.append(max_index + 1)
            need_remove = comp_rooms[max_index]
            sorted_comp_rooms.remove(need_remove)
            cls_found = True
            break
    
    if not cls_found: found_rooms.append(0)
    
print("==================")
print(found_counter)
print(found_rooms)