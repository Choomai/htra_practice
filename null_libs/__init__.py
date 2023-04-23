from math import sqrt
import string

def FParser(content: str,mode: str, convFloat=True):
    tmp = content.split("\n")

    if "line" in mode: tmp_lst = [(float(elem) if convFloat else int(elem)) for elem in tmp[1].split(" ")]
    
    if mode == "n_line":
        tmp_n = int(tmp[0])
        return tmp_n,tmp_lst
    elif mode == "nx_line":
        nx_lst = tmp[0].split(" ")
        tmp_n = int(nx_lst[0])
        tmp_x = float(nx_lst[1])
        return tmp_n,tmp_x,tmp_lst
    elif mode == "n_arr":
        tmp_n = int(tmp.pop(0))
        res = [[(float(sub_elem) if convFloat else int(sub_elem))  for sub_elem in elem.split(" ")] for elem in tmp]
        return tmp_n, res
    else: raise NotImplementedError("Missing parameters or mode not found")

def isPrime(inp: int) -> bool:
    for i in range(2, inp):
        if inp % i == 0: return False
    if inp > 1: return True
    else: return False

def oddNeven(inp: list) -> list:
    odd,even,neg,pos = [],[],[],[]
    for elem in inp:
        if elem % 2 == 0: even.append(elem)
        else: odd.append(elem)
        if elem >= 0: pos.append(elem)
        else: neg.append(elem)
    return [odd,even,neg,pos]

def divsr(inp, mode) -> list:
    res,odd,even = [],[],[]
    for i in range(1,inp+1):
        if inp % i == 0: 
            if i % 2 == 0: even.append(i)
            else: odd.append(i)
            res.append(i)
    if mode == "": return res
    elif mode == "od_ev": return [odd,even] # Short for odd and even.

def isPerfect(inp: int) -> bool:
    divs = divsr(inp, "")
    if sum(divs[:-1]) == inp: return True
    else: return False
def isSq(inp: int) -> bool:
    if (int(sqrt(inp)))**2 == inp: return True
    else: return False

def deCounter(inp: str) -> str:
    res = ""
    arr = list(inp)
    for i in range(len(arr) - 1):
        if (arr[i].isalpha()) and (arr[i + 1].isalpha()):
            res += arr[i]
            continue
        if (arr[i].isalpha()) and (arr[i + 1] in string.digits):
            res += arr[i] * int(arr[i + 1])
    return res