n = 6

fibs = [1, 1]
if n == 1 or n == 2:
    print(1)
    exit(0)

for i in range(3, n + 1):
    current = fibs[0] + fibs[1]
    fibs.pop(0)
    fibs.append(current)

print(fibs[1])