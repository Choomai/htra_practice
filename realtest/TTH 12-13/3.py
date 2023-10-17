def getInput(): return [int(elem) for elem in input().split()]

n, m = getInput()
students_cls = getInput()
comp_rooms = getInput()

found_counter = 0
for cls in students_cls:
    