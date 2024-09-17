n = int(1e7) + 1
divs = []

primes = []
sieve = [True] * (n)
for i in range(2, n):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i, n, i): sieve[j] = False

print(primes[:100])