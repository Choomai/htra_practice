input() # Ignore n, we don't need it.
inp_str = input()
caught_chars = ""
result,current_counter = 0,0

for char in inp_str:
    if char in caught_chars:
        caught_chars = caught_chars[caught_chars.index(char)+1:] + char
        current_counter = len(caught_chars)
        if current_counter > result: result = current_counter
        continue
    
    caught_chars += char
    current_counter += 1

print(result)