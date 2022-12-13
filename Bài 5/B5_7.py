import math as mt
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
p = a+b+c
print("Chu vi:",p)
print("Diện tích:",round(mt.sqrt(p*(p-a)*(p-b)*(p-c)),2))
