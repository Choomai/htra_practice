K, start, end = map(int, input().split())

def factorize(num: int) -> int:
    global K
    facts = {}
    div = 2
    while num > 1:
        if div > K: break
        while num % div == 0:
            facts[div] = facts.get(div, 0) + 1
            num //= div
        else: div += 1

    return facts if num == 1 else False

counter = 0
for num in range(start, end+1):
    if factorize(num): counter += 1
print(counter)