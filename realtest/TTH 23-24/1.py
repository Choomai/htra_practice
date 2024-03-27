n = 100
for i in range(2, n*n):
    divs_counter = 2
    for j in range(2, i // 2 + 1):
        if i % j == 0: divs_counter += 1

    if divs_counter == n:
        print(i)
        exit(0)