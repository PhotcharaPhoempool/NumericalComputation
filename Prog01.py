import math

def myrun(N):
    # True value of sin(2)
    true_val = math.sin(2.0)

    # Taylor series of sin(x) about x = pi/2, where h = 2 - pi/2
    a = math.pi / 2.0
    h = 2.0 - a

    # 5 significant digits tolerance: 0.5 × 10^(2-5) = 0.0005 %
    THRESHOLD = 0.5 * 10**(2 - 5)

    approx = 0.0          # accumulated approximation
    sign = 1              # (-1)^k, starts with +1 for the first term

    print(f"math.sin(2) = {true_val:.7f}")
    print("========================================")
    print(f"{'n':>3} {'ApproxV':>10} {'AbTrueErr%':>12} {'m':>3}")
    print("========================================")

    for k in range(N):
        m = 2 * k                 # derivative order (0, 2, 4, 6, ...)
        n = 2 * k + 1             # label column n: 1, 3, 5, 7, ...

        # Taylor term: (-1)^k * h^(2k) / (2k)!
        term = sign * (h ** m) / math.factorial(m)
        approx += term

        # relative true error in percent
        err = abs((true_val - approx) / true_val) * 100.0

        # print a row similar to the example
        print(f"{n:3d} {approx:10.7f} {err:12.7f}% {m:3d}")

        # stopping criterion: 5 significant digits
        if err < THRESHOLD:
            break

        # update sign for next term
        sign *= -1

    # print final result summary
    print("\nFinal approximation =", approx)
    print("Number of terms used =", k + 1)

    return approx

if __name__ == "__main__":
    myrun(20)
