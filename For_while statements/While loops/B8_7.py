for a in range(21): # Tối đa 100 / 5 = 20
    for b in range(100): # Tối đa 100 / 3 = 33.33
        for c in range(0,100,3):
            if (a + b + c == 100) and (5*a + 3*b + c/3 == 100):
                print(a,b,c)
# Trăm trâu trăm cỏ, Trâu đứng ăn năm, Trâu nằm ăn ba, Lụ khụ trâu già, Ba con một bó
# Mỗi loại trâu có ? con
# a đứng | b nằm | c già
# Có 100 bó cỏ, 100 con trâu
# 1 đứng ăn 5 bó, 1 nằm ăn 3 bó, 1/3 già ăn 1 bó