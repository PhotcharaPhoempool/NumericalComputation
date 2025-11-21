from math import sqrt

f = lambda x: 0.0 if x == 0 else 1 / sqrt(x)

def trapezoid(n, a, b):
    h = (b - a) / n
    p2 = f(a) + f(b)
    for k in range(1, n):
        p2 += 2 * f(a + k * h)
    return (h / 2) * p2

def calM(E):
    m, T = 0, 5
    while T > E:
        T /= 10
        m += 1
    return m

TV = 2 * sqrt(2)       # true value
a, b = 0.0, 2.0

n = 1
while True:
    CA  = trapezoid(n, a, b)
    Et  = TV - CA
    AEt = abs(Et / TV) * 100
    m   = calM(AEt)

    print(f"{n:7d}  {CA:10.5f}  {Et:10.5f}  {AEt:9.5f}  {m}")

    if m >= 2:          # break if m ≥ 2 significant digits
        break

    n *= 2              # add segment (1,2,4,8,...)
