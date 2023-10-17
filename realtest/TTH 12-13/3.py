def getInput(): return [int(elem) for elem in input().split()]

n, m = getInput()
students_cls = getInput()
comp_rooms = getInput()
sorted_comp_rooms = sorted(comp_rooms, reverse=True)

found_counter = 0
found_rooms = []

for cls in students_cls:
    max_diff, max_index = float('inf'), -1
    for comp in sorted_comp_rooms:
        if (comp >= cls + 1) and (max_diff > comp - cls - 1): max_index = comp_rooms.index(comp)
    
    if max_index != -1:
        found_counter += 1
        found_rooms.append(max_index + 1)
        need_remove = comp_rooms[max_index]
        comp_rooms.remove(need_remove)
        sorted_comp_rooms.remove(need_remove)

print("==================")
print(found_counter)
print(found_rooms)