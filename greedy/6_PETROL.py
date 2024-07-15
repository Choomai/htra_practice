with open("io/6_PETROL.inp", "r") as f:
    N, k = map(int, f.readline().split(" "))

    selected_tank = max(map(int, f.readline().split(" ")))

counter = 0
while k > 0:
    k -= selected_tank
    counter += 1

with open("io/6_PETROL.out", "w") as f: f.write(str(counter))