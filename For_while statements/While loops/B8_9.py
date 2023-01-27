import string
alp = list(string.ascii_uppercase)
for i,char in enumerate(alp):
    if (i % 10 == 0) and (i > 0): print()
    print(char,end=" ")