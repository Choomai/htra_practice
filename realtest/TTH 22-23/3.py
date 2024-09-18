with open("io/3_MESS.INP", "r") as f:
    n = f.readline().split()[0]
    lst = [int(k.split()[1]) for k in f.read().split("\n")]

cnt = 0
for i in range(1,int(n)+1):
    if not i in lst: cnt += 1

with open("io/3_MESS.OUT", "w") as f: f.write(str(cnt))