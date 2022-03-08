from itertools import combinations
import numpy as np

def men_dis(a_loc, b_loc) :

    distance = int(abs(a_loc[0]-b_loc[0]) + abs(a_loc[1]-b_loc[1]))

    return distance

def isolation_check(place, a_loc, b_loc) :

    if men_dis(a_loc, b_loc) > 2 :
        pass
    elif men_dis(a_loc, b_loc) == 1 :
        pass
    elif a_loc[0]==b_loc[0] or a_loc[1]==b_loc[1] :
        if place[int(abs(a_loc[0]+b_loc[0])/2)][int(abs(a_loc[1]+b_loc[1])/2)] == 'X':
            pass
        else : return False
    else :
        if place[a_loc[0]][b_loc[1]]=='X' and place[a_loc[1]][b_loc[0]]=='X':
            pass
        else : return False

def solution(places) :

    results = []

    for place in places :

        place = [list(x) for x in place]
        p_loc = []
        result = []

        for i, b in enumerate(place):

            for j, c in enumerate(list(b)):

                if c == 'P':
                    p_loc.append([i, j])

        p_com = list(combinations(p_loc, 2))

        for i in list(p_com):
            if isolation_check(place, i[0], i[1]) == False:
                result.append(0)
            else:
                result.append(1)

        if p_loc == [] : results.append(1)
        elif np.mean(result) == 1 : results.append(1)
        else : results.append(0)

    return results

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))



