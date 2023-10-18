# Create a value-to-symbol table.

# Take a integer and base to convert to.
# Create an array to store the digits in.
# While the integer is not zero:
#     Divide the integer by the base to:
#         (1) Find the "last" digit in your number (value).
#         (2) Store remaining number not "chopped" (integer).
#     Save the digit in your storage array.
# Return your joined digits after putting them in the right order.

from string import ascii_lowercase
num = int(input())
base26 = ""
while num > 0:
    num -= 1
    base26 = ascii_lowercase[num % 26] + base26
    num //= 26
print(base26)