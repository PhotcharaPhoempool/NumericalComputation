from math import exp

f = lambda x: 300 * x / (1 + exp(x))

def trapezoid(n, a, b):
    h = (b - a) / n
    p2 = f(a) + f(b)
    for k in range(1, n):
        p2 += 2 * f(a + k * h)
    return (h / 2) * p2

def calM(E):
    m, T =0, 5
    while T > E:
        T /= 10
        m += 1
    return m

TV = 246.59
for i in range(10):
    n = 2 ** i
    a, b = 0, 10
    CA = trapezoid(n, a, b)
    Et = TV - CA
    AEt = abs(Et / TV) * 100
    m = calM(AEt)
    print(f"{n:3d} {CA:7.3f} {Et:7.3f} {AEt:6.3f} {m}")