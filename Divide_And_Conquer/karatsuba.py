

def mul(x:str, y:str) -> str:
    """
    Calcalates multiplication of two integer numbers. This is not real Karatsuba just
    another way how to multiply numbers.

    Arguments:
        x:str - first agrument to be multilied
        y:str - second agrument to be multilied

    Returns:
        str - result of multiplication of x and y
    """
    # stop recursion if any input number has 1 digit
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    n = len(x) // 2
    m = len(y) // 2

    a = x[:n]
    b = x[n:]
    c = y[:m]
    d = y[m:]

    # pocet radov o ktore posuvam cisla je pocet cislic, ktore zostali napravo
    nn = len(x) - n
    mm = len(y) - m

    ac = mul(a, c) + '0' * (mm + nn)
    ad = mul(a, d) + '0' * nn
    bc = mul(b, c) + '0' * mm
    bd = mul(b, d)

    z = int(ac) + int(ad) + int(bc) + int(bd)

    return str(int(ac) + int(ad) + int(bc) + int(bd))



def mul_k(x:str, y:str) -> str:
    """
    Calcalates multiplication of two integer numbers. This is Karatsuba algorithm

    Arguments:
        x:str - first agrument to be multilied
        y:str - second agrument to be multilied

    Returns:
        str - result of multiplication of x and y
    """
    # stop recursion if any input number has 1 digit
    if len(x) == 1 or len(y) == 1:
        return str(int(x) * int(y))

    n = min(len(x) // 2, len(y) // 2)

    a = x[:-n]
    b = x[-n:]
    c = y[:-n]
    d = y[-n:]

    abcd = mul_k(str(int(a) + int(b)), str(int(c) + int(d)))

    ac = mul_k(a, c)
    bd = mul_k(b, d)
    middle = str(int(abcd) - int(ac) - int(bd))

    ac = ac + '0' * (2 * n)
    middle = middle + '0' * n

    return str(int(ac) + int(middle) + int(bd))

xx = '3141592653589793238462643383279502884197169399375105820974944592'
yy = '2718281828459045235360287471352662497757247093699959574966967627' 

# xx = '1234545781'
# yy = '56785232585641581'

print(f'mul  :{mul(xx, yy)}')
print(f'mul_k:{mul_k(xx, yy)}')





