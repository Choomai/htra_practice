inp = open("example/1_TIMX.INP", "r")
lst = inp.read().split(" ")
lst = [int(elem) for elem in lst] # Convert str to int
i,j = 0,0
while True:
    j = ((lst[0] * i + lst[1]) - lst[3]) / lst[2]
    if j == int(j): break
    elif j > 100000000: raise ValueError("Overflowed.")
    i += 1
out = open("example/1_TIMX.OUT", "w")
out.write(str(i) + " " + str(int(j)))
inp.close()
out.close()