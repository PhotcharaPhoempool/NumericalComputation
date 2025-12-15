def secant(x0, x1):
    f = lambda x: eval(s)
    # x0, x1 = 0.02, 0.05
    print(f"Solving the nonlinear equation {s}\nusing the secant method.")
    print('='*56)
    print(f" i|{'x0':^7}|{'x1':^7}|{'x2':^7}|{'f(x2)':^13}|{'Ea':^12}|m")
    print('='*56)
    for i in range(10):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        Ea = abs((x2 - x1)/x2)*100
        m = calM(Ea)
        print(f"{i+1:2d}|{x0:.5f}|{x1:.5f}|{x2:.5f}|{f(x2):13e}|{Ea:12e}|{m}")
        x0, x1 = x1, x2
        if m >= 8:
            break

def calM(E):
        m, T = 0, 5
        while T > E:
            m += 1
            T /= 10
        return m


if __name__=='__main__':
    #---- main begins here ------------------
    s  = '''x**3 -.165*x**2 +3.993e-4'''
    x0 = float(input("Input x0: "))
    x1 = float(input("Input x1: "))
    secant(x0,x1)