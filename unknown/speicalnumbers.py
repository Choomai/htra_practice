from math import sqrt

def sum_of_divisors(num):
    """Calculates the sum of divisors of a number, excluding the number itself."""
    sum_div = 0
    for i in range(1, int(sqrt(num))+1):
        if num % i != 0: continue

        sum_div += i + num//i
        if i == num//i: sum_div -= i
    return sum_div - num

N = 1
K = 50
for num in range(N, K+1):
    if sum_of_divisors(num) > num: print(num, end=" ")