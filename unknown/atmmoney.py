n = int(input()) // 1000

cashes = {
    10: 0, 20: 0, 50: 0,
    100: 0, 200: 0, 500: 0
}

while n >= 10:
    if n >= 500:
        n -= 500
        cashes[500] += 1
    elif n >= 200:
        n -= 200
        cashes[200] += 1
    elif n >= 100:
        n -= 100
        cashes[100] += 1
    elif n >= 50:
        n -= 50
        cashes[50] += 1
    elif n >= 20:
        n -= 20
        cashes[20] += 1
    elif n >= 10:
        n -= 10
        cashes[10] += 1

cashes_arr = cashes.values()
print(sum(cashes_arr))
print(*cashes_arr)