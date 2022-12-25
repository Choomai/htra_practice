import re
class timeCalc:
    def __init__(self, inp, type):
        if type == 0: type = 86400
        elif type == 1: type = 3600
        else: type = 60
        self.rem = inp % type
        self.calc = inp // type
inp = ""
while re.search("[a-zA-Z]",inp) or inp == "": inp = input("Nhập giây: ")
try: raw_secs = int(inp)
except ValueError:
    print("Invalid input. Value is converted to int.")
    raw_secs = int(float(inp))
d_all = timeCalc(raw_secs,0)
d = d_all.calc
d_rem = d_all.rem
h_all = timeCalc(d_rem,1)
h = h_all.calc
h_rem = h_all.rem
min_sec = timeCalc(h_rem,2)
m = min_sec.calc
s = min_sec.rem
print(f"{d}d {h}h {m}m {s}s",end="")