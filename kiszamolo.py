def kiszamolo(N_user, n_user, m_user, M_user, NA):
    def darab():
        global N
        if N_user > 0:
            N = N_user
        elif n_user > 0:
            N = n_user * NA
        elif m_user > 0 and M_user > 0:
            N = m_user/M_user * NA
        else:
            N = 0
        return(N)
    darab()
    def mol():
        global n
        if N > 0:
            n = N / NA
        else:
            n = 0
        return(n)
    mol()
    def tomeg():
        global m
        if m_user > 0:
            m = m_user
        elif n > 0 and M_user > 0:
            m = n * M_user
        else:
            m = 0
        return(m)
    tomeg()
    def MW():
        global M
        if M_user > 0:
            M = M_user
        elif m > 0 and n > 0:
            M = m / n
        else:
            M = 0
        return(M)
    MW()
    print("N = " + str(N)+ " db")
    print("n = " + str(n)+ " mol")
    print("m = " + str(m)+ " gramm")
    print("M = " + str(M)+ " gramm/mol")