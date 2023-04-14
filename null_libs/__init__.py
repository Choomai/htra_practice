def FParser(content: str,mode: str, convFloat=True):
    tmp = content.split("\n")
    if convFloat: tmp_lst = [float(elem) for elem in tmp[1].split(" ")]
    else: tmp_lst = [int(elem) for elem in tmp[1].split(" ")]
    if mode == "n_arr":
        tmp_n = int(tmp[0])
        return tmp_n,tmp_lst
    elif mode == "nx_arr":
        nx_lst = tmp[0].split(" ")
        tmp_n = int(nx_lst[0])
        tmp_x = float(nx_lst[1])
        return tmp_n,tmp_x,tmp_lst

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