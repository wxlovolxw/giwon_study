from itertools import *

def solution(k, dungeons):

    permuts = list(permutations(dungeons))

    count_list = []

    for permut in permuts:

        count = 0
        fat = k

        for i in permut:

            if fat >= i[0] :
                fat -= i[1]
                count += 1

        count_list.append(count)

    return max(count_list)