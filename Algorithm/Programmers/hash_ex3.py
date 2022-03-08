def solution(clothes):

    dict = {}
    count_clothes = list(map(lambda x : x[1], clothes))

    for cloth in clothes :
        dict[cloth[1]] = count_clothes.count(cloth[1])

    answer = 1

    for i in dict :
        answer *= dict[i]+1

    return answer-1

print(solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]))