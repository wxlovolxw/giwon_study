def solution(participant, completion):

    answer = ''
    sum_hash = 0
    dict= {}

    for name in participant :
        dict[hash(name)] = name
        sum_hash += hash(name)

    for name in completion :
        sum_hash -= hash(name)

    answer = dict[sum_hash]
    return answer


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))