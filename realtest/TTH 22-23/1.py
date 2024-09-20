with open("io/1_TIMX.INP", "r") as f:
    lst = f.read().split(" ")
    a1, b1, a2, b2 = [int(elem) for elem in lst]
i,j = 0,0

special_case = False
if a2 == 0: 

while not special_case:
    j = ((a1 * i + b1) - b2) / a2
    if j == int(j): break
    i += 1
with open("io/1_TIMX.OUT", "w") as f:
    f.write(f"{i} {int(j)}")