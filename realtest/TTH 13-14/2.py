base26 = {i: char for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}

def int2str(integer):
    array = []
    while integer:
        integer, value = divmod(integer, 26)
        array.append(base26[value - 1])
    return ''.join(reversed(array))

print(int2str(int(input())))
# Create a value-to-symbol table.

# Take a integer and base to convert to.
# Create an array to store the digits in.
# While the integer is not zero:
#     Divide the integer by the base to:
#         (1) Find the "last" digit in your number (value).
#         (2) Store remaining number not "chopped" (integer).
#     Save the digit in your storage array.
# Return your joined digits after putting them in the right order.