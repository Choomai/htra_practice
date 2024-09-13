def divisor_counts(n):
    n += 1
    divisor_counts = [1] * n
    divisor_counts[0] = None
    for i in range(2, n):
        for j in range(i, n, i):
            divisor_counts[j] += 1
    return divisor_counts

n = int(1e7)
print(divisor_counts(n))