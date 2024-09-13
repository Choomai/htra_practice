N = int(5)  # Giới hạn N
a = [1] * (N + 1)


def sang(n):
    for i in range(1, int(n**0.5) + 1):
        for j in range(2 * i, n + 1, i):
            a[j] += 1

# Thực hiện sàng
sang(N)

# Đọc vào giá trị n
n = 3

# Tìm số đầu tiên có đúng n ước
for i in range(1, N + 1):
    if a[i] == n:
        print(i)
        print(a[1:100])
        break