from sys import path
path.append("../../")
from null_practice.null_libs import isPrime

N = 10000
result = [N]
current = N - 1
while current > 1:
    if isPrime(current) or any(current % num == 0 for num in result):
        result.append(current)
    current -= 1
print(" ".join(map(str, result)), len(result), sep="\n")