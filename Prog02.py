from math  import log

f = lambda x: 2000 * log(140000 / (140000 - 2100 * x)) - 9.8 * x

def trapezoid(n, a, b):
    h = (b - a) / n
    p2 = f(a) + f(b)
    for i in range(1, n):
        p2 += 2 * f(a + i * h)
    return (h / 2) * p2

a, b, TV = 8, 30, 11061

for n in range(1, 9):
    CA = trapezoid(n, a, b)
    ET = TV - CA
    AEt = abs(ET / TV) * 100
    if n == 1:
        print(f"{n} {CA:.1f} {ET:6.1f} {AEt:.3f} {'--':^6}")
        PA = CA
        continue
    AEa = abs((CA - PA) / CA) * 100
    print(f"{n} {CA:.1f} {ET:6.1f} {AEt:.3f} {AEa:.4f}")
    PA = CA
