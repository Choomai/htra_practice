from itertools import product

def isUnique(inp) -> bool:
    inp = "".join( map(str, list(inp)) ) # Use for itertools.product input.
    n = len(inp)
    for length in range(1, n // 2 + 1):  # length of substring
        for i in range(n - 2 * length + 1):  # start index of first substring
            if inp[i:i+length] == inp[i+length:i+2*length]: return False
    return True

counter = 1
n, m = [int(elem) for elem in input().split()]
for valid_str in filter(isUnique, product(range(1, m + 1), repeat=n)):
    print("".join( map(str, valid_str) ))