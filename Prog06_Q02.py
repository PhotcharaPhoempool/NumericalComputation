def myRun():
    print("Welcome to CDTI68's Nonlienear Equation Solver")
    print("(1) Secant Method")
    print("(2) Newton-Raphson method")
    choice = input("Your choice (1 or 2): ")

    if choice == '1':
        s = input("Input your f(x) using correct Python expression:\n")
        f = lambda x: eval(s)
        x0 = float(input("Input x0: "))
        x1 = float(input("Input x1: "))
        
        print(f"Solving the nonlinear equation {s}\nusing the secant method.")
        print("="*56)
        print(f" i|{'x0':^7}|{'x1':^7}|{'x2':^7}|{'f(x2)':^13}|{'Ea':^12}|{'m'}")
        print("="*56)

        
        for i in range(10):
            x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
            Ea = abs((x2 - x1)/x2)*100
            m = calM(Ea)
        
            print(f"{i+1:2d}|{x0:.5f}|{x1:.5f}|{x2:.5f}|{f(x2):13e}|{Ea:12e}|{m}")
            x0,x1 = x1,x2
            if m >= 8:
                break

    elif choice == '2':
        s = input("Input your f(x) using correct Python expression:\n")
        f = lambda x: eval(s)
        s1 = input("Input your f'(x) using correct Python expression:\n")
        f1 = lambda x: eval(s1)
        x0 = float(input("Input x0: "))

        print(f"Solving the nonlinear equation {s}\nusing the newton-raphson method.")
        print("="*48)
        print(f" i|{'x0':^7}|{'x1':^7}|{'f(x1)':^13}|{'Ea':^12}|{'m'}")
        print("="*48)

        for i in range(10):
            x1 = x0 - f(x0)/f1(x0) 
            Ea = abs((x1 - x0)/x1)*100
            m = calM(Ea)
            
            print(f"{i+1:2d}|{x0:.5f}|{x1:.5f}|{f(x1):13e}|{Ea:12e}|{m}")
            x0 = x1
            if m >= 8:
                break


def calM(E):
    m, T = 0,5
    while T > E:
        m += 1
        T /= 10

    return m

if __name__=='__main__':         
    myRun()