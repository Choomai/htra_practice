for i in range(10):
    for j in range(1,11):
        if i*10+j <= 10: print(i*10+j,"{:<4}".format(""),end=" ")
        else: print(i*10+j,"{:<4}".format(""),sep="",end=" ")
    print()