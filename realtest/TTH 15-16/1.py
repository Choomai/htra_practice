# What is this ? Can't understand what the problem is...

import sys
from pprint import pprint

m = int(input())
key_dict = {1: " "}
for i in range(m): key_dict[i + 2] = input()
keyboard_input = input().split()
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