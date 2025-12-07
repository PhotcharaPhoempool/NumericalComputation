def myrun(N):
    '''Student code begins here'''
    f = lambda x: x**3 - 0.165*x**2 + 3.993e-4

    # แถวทั่วไป
    p = lambda i, L, U, M, Ea, m: print(
        f"{i:5d}     {L:.5f} {U:.5f} {M:.5f} {Ea:7.4f} {f(M):10.3e} {m}"
    )

    U, L = 0.11, 0
    oldM = (U + L) / 2

    print("Iteration    Xl      Xu      Xm     |Ea|     f(Xm)   m")
    print("======================================================")

    def calM(E):
        m, T = 0, 5
        while T > E:
            m += 1
            T /= 10
        return m
    
    for i in range(N):
        if i == 0:
            # แก้ตรงนี้: ลดช่องว่างหลัง "--" จาก 5 เป็น 4 ช่อง
            print(f"{i+1:5d}     {L:.5f} {U:.5f} {oldM:.5f}   --    {f(oldM):10.3e} -")
            #                                      ^^^^
            continue

        if f(L)*f(oldM) < 0:
            U = oldM
        else:
            L = oldM

        M = (U + L) / 2
        Ea = abs((M - oldM)/M) * 100
        m = calM(Ea)
        p(i+1, L, U, M, Ea, m)
        oldM = M

        if m >= 3:
            break

    '''Student code ends here'''


if __name__=='__main__':
    N = int(input("Enter a positive integer: "))
    print("======================================================")
    myrun(N)
