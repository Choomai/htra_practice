from math import gcd

a,b = map(int, input().split())
x = 0
result = gcd(a,b)
# equation: gcd(a,b) = a*x + b*y
# solve for x,y

while True:
    y = (result - a*x) / b
    neg_y = (result - a*(-x)) / b
    if int(y) == y: break
    elif int(neg_y) == neg_y:
        x *= -1
        break
    else: x += 1

print(x, int(y))