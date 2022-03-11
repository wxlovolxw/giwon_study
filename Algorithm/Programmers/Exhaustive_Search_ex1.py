def solution(answers):
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    counts = [0, 0, 0]

    for i, answer in enumerate(answers):

        if answer_1[i % 5] == answer: counts[0] += 1
        if answer_2[i % 8] == answer: counts[1] += 1
        if answer_3[i % 10] == answer: counts[2] += 1

    answer = []

    for i, count in enumerate(counts):

        if count == max(counts):
            answer.append(i + 1)

    return answer

print(solution([4]))