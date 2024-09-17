from textwrap import wrap

full_str = input()
counter = 0

for i in range(3, len(full_str)):
    for word in wrap(full_str, i):
        if word == word[::-1]: counter += 1
# consfused ?
print(counter)