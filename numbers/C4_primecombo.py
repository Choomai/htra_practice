from itertools import pairwise

N = int(input())

primes = []
sieve = [True] * 1_000_000
for i in range(2, 1_000_000):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i, 1_000_000, i): sieve[j] = False

for a,b in pairwise(primes):
    if abs(a-b) == N:
        print(a,b)
        exit(0)
    else: continue