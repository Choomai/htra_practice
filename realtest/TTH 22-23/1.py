inp = open("io/1_TIMX.INP", "r")
lst = inp.read().split(" ")
lst = [int(elem) for elem in lst]
i,j = 0,0
while True:
    j = ((lst[0] * i + lst[1]) - lst[3]) / lst[2]
    if j == int(j): break
    i += 1
out = open("io/1_TIMX.OUT", "w")
out.write(str(i) + " " + str(int(j)))
inp.close()
out.close()