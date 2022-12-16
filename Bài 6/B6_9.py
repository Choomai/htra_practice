scr = float(input("Nhập điểm trung bình: "))
res = "Yếu"
if scr > 9: res = "Giỏi"
elif 7 <= scr < 9: res = "Khá"
elif 5 <= scr < 7: res = "Trung bình"
print(res)