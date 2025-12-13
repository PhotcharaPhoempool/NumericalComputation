f = lambda x: x**3 - 0.03*x**2 + 2.4e-6
f1 = lambda x: 3*x**2 - 0.06*x
fp = lambda i, x, Ea: print(f"{i:>2d}|{x:8.5f}|{f(x):13.9f}|{Ea:7.3f}")

N = int(input("Enter a positive integer: "))

x0 = 0.01999

print("="*33)
print(f" i|{'Xi':^8}|{'f(Xi)':^13}|{'|Ea|%':^7}")
print("="*33)

print(f"{'0':>2}|{x0:8.5f}|{f(x0):13.9f}|{'--':^7}")
for i in range(1, N+1):
    x1 = x0 - f(x0)/f1(x0)
    Ea = abs((x1 - x0)/x1) * 100
    x0 = x1
    fp (i, x1, Ea)
print("="*33)