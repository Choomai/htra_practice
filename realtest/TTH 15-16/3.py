m, n = [int(elem) for elem in input().split()]
s = int(input())
matrix = []
for _ in range(m): matrix.append([int(elem) for elem in input().split()])
# Y axis first.
max_block_area = float('inf')

def getBlock(left_x, top_y, right_x, bottom_y):
    block = []
    for y in range(top_y, bottom_y+1):
        block.extend(matrix[y][left_x:right_x+1])
    return block

for block_size in range(1, min(n, m)):
    for top_y in range(0, m - block_size):
        bottom_y = top_y + block_size
        for left_x in range(0, n - block_size):
            right_x = left_x + block_size
            block = getBlock(left_x, top_y, right_x, bottom_y)
            sum_block = sum(block)
            if sum_block == s:
                print(right_x ** 2)
                print(sum_block)
                exit(0)
            elif sum_block < s:
                if max_block_area > right_x ** 2: max_block_area = right_x ** 2

print(max_block_area)