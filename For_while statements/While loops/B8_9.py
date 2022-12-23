import string
alp = list(string.ascii_uppercase)
for i in range(len(alp)):
    if (i % 10 == 0) and (i > 0): print()
    print(alp[i],end=" ")