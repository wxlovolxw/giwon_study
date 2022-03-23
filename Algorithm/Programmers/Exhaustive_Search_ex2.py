from itertools import *

def isprime(num):

    for i in range(2,round(num//2)+1):
        if num % i == 0 :
            return False
            break
        else : pass

    return True

def solution(answers):
    length = len(answers)

    nums = list(answers)

    count = 0

    for answer in answers:
        if int(answer) == (0 or 1): pass

        elif isprime(int(answer)) == True:
            count += 1

    for i in range(length - 1):

        permuts = list(permutations(nums, i + 2))

        for i, permut in enumerate(permuts):
            permut_list = list(permut)
            joined_permut_list = "".join(permut_list)

            if isprime(int(joined_permut_list)) == True:
                count += 1

    return count

print(solution("017"))


