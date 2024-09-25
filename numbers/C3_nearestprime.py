N = int(input()) + 1

prime = []
sieve = [True] * N
for i in range(2, N):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i, N, i): sieve[j] = False

print(prime)