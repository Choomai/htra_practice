inp = open("DOITHO.INP", "r")
out = open("DOITHO.OUT", "w")
n = int(inp.read())
rab = [0]
for i in range(1,n+1):
    rab = [elem + 1 for elem in rab]
    for elem in rab:
        if elem > 2: rab.append(0)
    out.write(str(len(rab)) + " ")
inp.close()
out.close()