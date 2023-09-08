inp_str = input()
caught_chars = ""
result,current_counter = 0,0

for char in inp_str:
    if char in caught_chars:
        if current_counter > result: result = current_counter
        caught_chars = caught_chars[1:]
        current_counter = len(caught_chars)
        caught_chars += char
        continue
    
    caught_chars += char
    current_counter += 1

print(result)