# n = 3, print "000 001 010 ... 111"
# n = 5, print "00000 00001 00010 ... 11111"

n = int(input())

for i in range(1, 2**n):
    # 0>{n}, means prefix with 0 to meet the width requirement of n
    # b, means format as binary.
    print(f"{i:0>{n}b}", end=" ")