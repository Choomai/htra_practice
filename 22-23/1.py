inp = open("TIMX.INP", "r")
lst = inp.read().split(" ")
lst = [int(elem) for elem in lst] # Convert str to int
i,j = 0,0
cond = False
while not cond:
    if (lst[0] * i + lst[1]) == (lst[2] * j + lst[3]):
        cond = True
        break
    if i == j:
        j += 1
        continue
    if i > j:
        j += 1
        continue
    if i < j:
        i += 1
        j -= 1
        continue
out = open("TIMX.OUT", "w")
out.write(str(i) + " " + str(j))
inp.close()
out.close()