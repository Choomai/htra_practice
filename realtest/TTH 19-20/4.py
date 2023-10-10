def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

# N = int(input())
N = 10000
result = [N]
current = N - 1
while current > 1:
    if isPrime(current) or any(current % num == 0 for num in result):
        result.append(current)
    current -= 1
print(result)