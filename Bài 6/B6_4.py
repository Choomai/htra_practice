from math import sqrt
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
# End inp
delta = b**2-4*a*c
if delta < 0: print("PT vô nghiệm.")
elif delta > 0:
    x = [(-b+sqrt(delta))/2*a,(-b-sqrt(delta))/2*a]
    print("PT có 2 nghiệm")
    print(f"x[0]={x[0]}")
    print(f"x[1]={x[1]}")
else:
    x = -(b/2*a)
    print(f"PT có nghiệm kép, x={x}")