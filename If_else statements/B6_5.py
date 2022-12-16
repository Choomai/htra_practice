import re # Regex import
inp = ""
while (len(inp) != 1):
    inp = input("Nhập 1 kí tự: ")
    if (len(inp) > 1): print("Lỗi. Nhập lại.") # Optimal
# regex = r"[a-zA-Z]"
# res = bool(re.search(regex,inp))
# print("Kí tự nằm trong [a-Z]" if res else "Kí tự không nằm trong [a-Z]")
print("Kí tự nằm trong [a-Z]" if inp.isalpha() else "Kí tự không nằm trong [a-Z]")