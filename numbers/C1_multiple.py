import re

N = int(input())
pattern = re.compile("[09]*")
i = 1
while True:
    current_multipler = N * i
    if re.fullmatch(pattern, str(current_multipler)):
        print(current_multipler)
        exit(0)
    else: i += 1