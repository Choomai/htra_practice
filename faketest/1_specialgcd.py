A,B = map(int, input().split())

max_sum = 0
for i in range(2, min(A,B)+1):
    if A % i == 0 and B % i == 0:
        # Convert from 220 -> "220" -> ["2", "2", "0"] -> [2, 2, 0]
        current_sum = sum(map(int, tuple(str(i))))
        if current_sum > max_sum: max_sum = current_sum

print(max_sum)