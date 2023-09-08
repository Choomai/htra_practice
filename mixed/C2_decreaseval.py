n = int(input())
counter = 0

while n != 0:
    counter += 1
    # Convert the current number to string
    # Split the string and convert each char to int
    # Get the highest number and subtract to n
    n -= max([int(elem) for elem in list(str(n))])
    
print(counter)