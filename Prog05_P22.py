f = lambda x: (x-1)**3 + 0.512
f1 = lambda x: 3*(x-1)**2
fp = lambda i, x, E: print(f"{i:>2d}|{x:8.4f}|{f(x):9.2f}|{E:8.4f}")

N = int(input("Enter a positive integer: "))
x0 = 5
print("="*30)
print(f" i|{'Xi':^8}|{'f(Xi)':^9}|{'|Ea|%':^8}")
print("="*30)
print(f"{'0':>2}|{x0:8.4f}|{f(x0):9.2f}|{'--':^8}")
for i in range(1, N):
    x1 = x0 - f(x0)/f1(x0)
    Ea = abs((x1 - x0)/x1) * 100
    x0 = x1
    if i > 6 and i%2 == 1:
        continue
    fp(i, x1, Ea)
print("="*30)