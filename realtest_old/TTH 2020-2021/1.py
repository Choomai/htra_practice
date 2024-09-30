from itertools import pairwise

N = int(input())

prime = []
sieve = [True] * N
for i in range(2, N):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i, N, i): sieve[j] = False

result = []
for a,b in pairwise(prime):
    if b - a == 2: result.append((a,b))

for index, result in enumerate(result, 1):
    print(f"{index}: [{result[0]}, {result[1]}]")