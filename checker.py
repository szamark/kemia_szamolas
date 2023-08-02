def checker(N_user, n_user, m_user, M_user, NA):
    if N_user > 0 and n_user > 0:
        if n_user != N_user/NA:
            print("Az adatok nem konzisztensek")
            exit()
    elif n_user > 0 and m_user > 0 and M_user > 0:
        if n_user != m_user/M_user:
            print("Az adatok nem konzisztensek")
            exit()
    elif N_user > 0 and m_user > 0 and M_user > 0:
        if N_user/NA != m_user/M_user:
            print("Az adatok nem konzisztensek")
            exit()
    else:
        pass