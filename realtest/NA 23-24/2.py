import re
n = int(input())
wordlists = []
for _ in range(n): wordlists.append(input())

def longest_substring(input_string):
    substrings = re.split('[ARW]', input_string)
    return max(substrings, key=len) or "NO"

found_words = []

for word in wordlists:
    found_words.append(longest_substring(word))
