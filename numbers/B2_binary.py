with open("io/B2_binary.inp", "r") as f:
    n = int(f.readline())
    result = int(f.readline(), base=2) + 1
    if result >= 2**n: result = 0
    print(f"{result:0{n}b}")