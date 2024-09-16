with open("io/1_TIMX.INP", "r") as f:
    lst = f.read().split(" ")
    lst = [int(elem) for elem in lst]
i,j = 0,0
while True:
    j = ((lst[0] * i + lst[1]) - lst[3]) / lst[2]
    if j == int(j): break
    i += 1
with open("io/1_TIMX.OUT", "w") as f:
    f.write(f"{i} {int(j)}")