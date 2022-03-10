def solution(answers):

    length = len(answers)

    a = [2,1,2,3,2,4,2,5]
    b = [3,3,1,1,2,2,4,4,5,5]

    list_1 = [1,2,3,4,5] *(length//5) + list(range(length%5))
    list_2 = a*(length//8)+a[:(length%8)]
    list_3 = b*(length//10)+b[:length%10]

    count_1 = 0
    count_2 = 0
    count_3 = 0

    for i,a in enumerate(answers):
        if list_1[i] == a:
            count_1 += 1

    for i,a in enumerate(answers):
        if list_2[i] == a:
            count_2 += 1

    for i,a in enumerate(answers):
        if list_3[i] == a:
            count_3 += 1

    count_list = [count_1, count_2, count_3]
    answer = []
    for i,count in enumerate(count_list):
        if max(count_list) == count:
            answer.append(i+1)

    return answer

print(solution([1,3,2,4,2]))