n = 8

fibs = [1, 1]
if n == 1 or n == 2:
    print(True)
    exit(0)

while fibs[1] < n:
    current = fibs[0] + fibs[1]
    fibs.pop(0)
    fibs.append(current)

if fibs[1] == n: print(True)
else: print(False)