from functools import lru_cache

with open("io/BUILD.inp", "r") as f:
    n = int(f.readline())    
    tests = list(map(int, f.read().split()))

@lru_cache(maxsize=1024)
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1

    return fib(n-1) + fib(n-2)

for test in tests:
    print(fib(test+1))