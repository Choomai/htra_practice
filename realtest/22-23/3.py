inp = open("io/3_MESS.INP", "r")
n = inp.readline().split(" ")[0]
raw_lst = inp.read().split("\n")
cnt,lst = 0,[]
for raw in raw_lst:
    temp = raw.split(" ")
    lst.append(int(temp[1]))
for i in range(1,int(n)+1):
    if not i in lst: cnt += 1
out = open("io/3_MESS.OUT", "w")
out.write(str(cnt))
inp.close()
out.close()