from math import gcd

N = int(input())

counter = 1
primes = []
sieve = [True] * N
for i in range(2, N):
    if sieve[i]:
        primes.append(i)
        if gcd(i, N) == 1: counter += 1
        for j in range(i*i, N, i): sieve[j] = False

print(primes)
print(counter)