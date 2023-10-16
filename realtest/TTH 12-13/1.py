io = {
    "in": open("io/1_GIAITHUA.inp", "r"),
    "out": open("io/1_GIAITHUA.out", "w")
}
fact_preCalc = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def fact_non0LastDigit(n):
    if n < 10: return fact_preCalc[n]

    if int(str(n)[-2]) % 2 == 0:
        equation = 4 * fact_non0LastDigit(n // 5) * fact_non0LastDigit(int(str(n)[-1]))
        return int(str(equation)[-1])
    else:
        equation = 6 * fact_non0LastDigit(n // 5) * fact_non0LastDigit(int(str(n)[-1]))
        return int(str(equation)[-1])
    
for num in io["in"]:
    io["out"].write(str(fact_non0LastDigit(int(num))) + "\n")

io["in"].close()
io["out"].close()