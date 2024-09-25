N = int(input()) + 1

primes = []
sieve = [True] * N
for i in range(2, N):
    if sieve[i]:
        primes.append(i)
        for j in range(i*i, N, i): sieve[j] = False

print(primes[-1])