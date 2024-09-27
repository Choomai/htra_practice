from itertools import combinations_with_replacement

N = 100_000

primes = set()
sieve = [True] * N

for i in range(2, N):
    if sieve[i]:
        primes.add(i)
        for j in range(i*i, N, i): sieve[j] = False

def check(comb: tuple) -> bool:
    global N
    return sum(comb) == N

print(len(tuple(filter(check, combinations_with_replacement(primes, 2)))))