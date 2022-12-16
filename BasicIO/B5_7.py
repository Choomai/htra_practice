from math import sqrt
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
p = a+b+c
print("Chu vi:",p)
print("Diện tích:",round(sqrt(p*(p-a)*(p-b)*(p-c)),2))
