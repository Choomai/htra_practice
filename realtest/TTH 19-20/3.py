n = int(input())
syms = []
for _ in range(n): syms.append(input())

def make_palindrome(s):
    if s == s[::-1]: return s # Quit recursion
    
    if s[0] == s[-1]:
        # If the first and last characters are the same
        # Find the palindrome but remove first and last char, but still keeping the char at output
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    else: 
        # If the first and last characters are different
        pal1 = s[0] + make_palindrome(s[1:]) + s[0]
        pal2 = s[-1] + make_palindrome(s[:-1]) + s[-1]
        # Return the palindrome that requires fewer insertions
        return pal1 if len(pal1) < len(pal2) else pal2

for sym_str in syms: 
    print(make_palindrome(sym_str))