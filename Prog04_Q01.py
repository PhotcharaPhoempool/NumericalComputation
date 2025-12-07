f = lambda x: x**3 - 0.165*x**2 + 3.993e-4
p = lambda i, L, U, M, Ea, m: print(f"{i:^10d} {L:7.5f} {U:7.5f} {M:7.5f} {Ea:7.4f} {f(M):10.3e} {m}")
N = 20
U, L = 0.11, 0
oldM = (U + L) / 2
print(f"Iteration {'Xl' :^7} {'Xu':^7} {'Xm':^7} {'|Ea|' :^7} {'f(Xm)':^10} {'m'}")

def calM(E):
    m, T = 0, 5
    while T > E:
        m += 1
        T /= 10
    return m

for i in range(N):
    if i == 0:
        print(f"{i+1:^10d} {L:7.5f} {U:7.5f} {oldM:7.5f} {'--':^7} {f(oldM):10.3e} -")
        continue
    if f(L)*f(oldM) < 0:
        U = oldM
    else:
        L = oldM
    M = (U + L) / 2
    Ea = abs((M - oldM)/ M) * 100
    m = calM(Ea)
    p(i+1, L, U, M, Ea, m)
    oldM = M

    ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc