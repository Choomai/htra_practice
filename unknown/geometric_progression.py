def progression(size, multiplier):
    result, last_num = 1, 1
    for _ in range(size-1):
        result += last_num * multiplier
        last_num *= multiplier
        
    return result

print(progression(*map(int, input().split())))