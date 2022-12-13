class timeCalc:
    def __init__(self, inp, type):
        if type == 0: type = 86400
        elif type == 1: type = 3600
        else: type = 60
        self.rem = inp % type
        self.calc = inp // type
raw_secs = int(input("Nhập giây: "))
d = timeCalc(raw_secs,0).calc
d_rem = timeCalc(raw_secs,0).rem
h = timeCalc(d_rem,1).calc
h_rem = timeCalc(d_rem,1).rem
m = timeCalc(h_rem,2).calc
s = timeCalc(h_rem,2).rem
print(f"{d}d {h}h {m}m {s}s",end="")