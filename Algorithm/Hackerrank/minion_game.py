def minion_game(S) :
    S_list = list(S)

    Point_Stuart = 0    # 자음값의 합. 0으로 초기화
    Point_Kevin = 0     # 모음값의 합. 0으로 초기화

    for n, word in enumerate(S_list):
        if word in ("A","E","I","O","U") :  # 안에 있다면 모음.
            Point_Kevin += len(S_list) - n

        else :
            Point_Stuart += len(S_list) - n

    if Point_Stuart > Point_Kevin :
        print("Stuart", Point_Stuart)

    elif Point_Stuart < Point_Kevin :
        print("Kevin", Point_Kevin)

    else : print("Draw")


print(minion_game("BANANA"))
