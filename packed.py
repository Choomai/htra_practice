# factorial(inp) === 1 * 2 * 3 * ... * inp
# prod(...inp): multiply all elements.
from math import factorial,prod
def divsr(inp, mode):
    res,odd,even = [],[],[]
    for i in range(1,n+1):
        if inp % i == 0: 
            if i % 2 == 0: even.append(i)
            else: odd.append(i)
            res.append(i)
    if mode == "": return res
    elif mode == "od_ev": return [odd,even] # Short for odd and even.
class Calc:
    def __init__(self, n, x, a, b):
        s = [0] * 31
        # Problem 1
        for i in range(1,n+1): s[1] += i
        self.prb1 = s[1]

        # Problem 2
        for i in range(1,n+1): s[2] += i**2
        self.prb2 = s[2]

        # Problen 3
        for i in range(1,n+1): s[3] += 1/i
        self.prb3 = s[3]

        # Problem 4
        for i in range(1,n+1): s[4] += 1/(2*i)
        self.prb4 = s[4]

        # Problen 5
        for i in range(1,n+1): s[5] += 1/(2*n+1)
        self.prb5 = s[5]

        # Problem 6
        for i in range(1,n+1): s[6] += 1/(i*(i+1))
        self.prb6 = s[6]

        # Problem 7
        for i in range(1,n+1): s[7] += i/(i+1)
        self.prb7 = s[7]

        # Problem 8
        for i in range(n+1): s[8] += (2*i+1)/(2*i+2)
        self.prb8 = s[8]

        # Problem 9
        self.prb9 = factorial(n)

        # Problem 10
        self.prb10 = x**n

        # Problem 11
        for i in range(1,n+1): s[11] += factorial(i)
        self.prb11 = s[11]

        # Problem 12
        for i in range(1,n+1): s[12] += x**i
        self.prb12 = s[12]

        # prb13 to 16 cache
        cache13_16 = divsr(n, "")
        # Problem 13
        self.prb13 = cache13_16

        # Problem 14
        self.prb14 = sum(cache13_16)

        # Problem 15
        self.prb15 = prod(cache13_16)

        # Problem 16
        self.prb16 = len(cache13_16)

        # prb17 to 21 cache
        cache17_21 = divsr(n, "od_ev")
        # Problem 17
        self.prb17 = divsr[0]
        
        # Problem 18
        self.prb18 = sum(cache17_21[1])
        
        # Problem 19
        self.prb19 = prod(cache17_21[0])

        # Problem 20
        self.prb20 = len(cache17_21[1])

        # Problem 21
        self.prb21 = max(cache17_21[0])

n,x,a,b = 0,0,0,0
# try: n = int(input())
# except ValueError: pass
def fallbackInp(content):
    temp = input(content)
    if temp: return int(temp)
    else: return 0
for i in range(4):
    if i == 0: n = fallbackInp("Nhập n: ")
    elif i == 1: x = fallbackInp("Nhập x: ")
    elif i == 2: a = fallbackInp("Nhập a: ")
    else: b = fallbackInp("Nhập b: ")
c = Calc(n,x,a,b)
print("Ctrl + C để thoát chương trình.")
while True:
    prb_id = int(input("Nhập ID bài tập: "))
    print(eval(f"c.prb{prb_id}"))