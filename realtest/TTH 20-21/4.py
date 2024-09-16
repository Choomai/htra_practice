with open("io/BUILD.inp", "r") as f:
    n = int(f.readline())    
    tests = list(map(int, f.read().split()))

cache = []
def fib(n):
    if n == 1: return 0
    elif n == 2: return 1
    