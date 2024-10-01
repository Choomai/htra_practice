from math import sqrt

with open("io/nearperfect.inp", "r") as f:
    N = int(f.readline())
    input_nums = tuple(map(int, f.readline().split()))

for num in input_nums:
    current_sum = 1 + num
    for i in range(2, int(sqrt(num))+1):
        # We can optimize the process by considering divisor pairs.
        # If i is a divisor of num, then num / i is also a divisor.
        # We only need to iterate up to the square root of num.
        # For example, 32 / 2 = 16 and 32 / 16 = 2.
        if num % i == 0: current_sum += i + num//i
    
    print(int(2*num <= current_sum))