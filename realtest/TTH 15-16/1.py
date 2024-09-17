
key_dict = {1: " "}
with open("io/1_T9.inp", "r") as f:
    m = int(f.readline())
    for i in range(2, m+2): key_dict[i] =
    keyboard_input = tuple(map(int, f.readline().split()))

cached_key, output = "", ""
index = 0
for key in keyboard_input:
    if not cached_key:
        cached_key = key
        index = 0
        continue
    
    output += key_dict[int(cached_key)][int(index)]
    if key == cached_key:
        index += 1
    else:
        cached_key = ""
        index = 0
    
    if key == "1": output += key_dict[1]

print(output)