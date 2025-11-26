from math import exp

f = lambda x: 300 * x / (1 + exp(x))

def header():
    print("="*29)
    print(f"{'Seg'} {'ApproxV'} {'Et':^7} {'|Et|':^6} m")
    print("="*29)

def trapezoid(n, a, b):
    h = (b - a) / n
    p2 = f(a) + f(b)
    for k in range(1, n):
        p2 += 2 * f(a + k * h)
    return (h / 2) * p2

def myrun(N):
    """This code fragment will run the Trapezoidal Rule
    of integration using maximum number of 2^N segments.
    However, the program will stop after |Et| reaching
    at least 4 significant digit correct! """
    TV = 246.59
    a, b = 0, 10

    # ลองทีละจำนวน segment: 1, 2, 4, 8, ..., 2^(N-1)
    for i in range(N):
        n = 2 ** i
        CA = trapezoid(n, a, b)
        Et = TV - CA                  # true error
        AEt = abs(Et / TV) * 100      # %relative true error

        # --- คำนวณ m (จำนวนหลักนัยสำคัญที่เชื่อถือได้) ---
        m, T = 0, 5
        while T > AEt:
            T /= 10
            m += 1
        # -----------------------------------------------

        print(f"{n:3d} {CA:7.3f} {Et:7.3f} {AEt:6.3f} {m}")

        # หยุดเมื่อได้อย่างน้อย 4 significant digits
        if m >= 4:
            break

##-- main
N = int(input("Input a positive integer N: "))
print(f"Maximum 2^{N} segments will be tested?")
header()
myrun(N)
