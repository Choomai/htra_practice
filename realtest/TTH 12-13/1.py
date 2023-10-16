fact_preCalc = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]

def fact_non0LastDigit(n):
    if n < 10: return fact_preCalc[n]

    if int(str(n)[-2]) % 2 == 0:
        return (4 * fact_non0LastDigit(n // 5) * fact_non0LastDigit(int(str(n)[-1])))
    else:
        return (6 * fact_non0LastDigit(n // 5) * fact_non0LastDigit(int(str(n)[-1])))