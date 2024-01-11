n = 1000001
divs = []

primes = []
sieve = [True] * (n)
for i in range(2, n):
    if sieve[i]:
        primes.append(i)
        for i in range(i*i, n, i): sieve[i] = False

print(primes)