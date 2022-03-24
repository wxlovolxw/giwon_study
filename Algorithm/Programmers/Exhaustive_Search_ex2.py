from itertools import *

def isprime(num):

    for i in range(2,round(pow(num,1/2))+1):
        if num % i == 0 :
            return False
            break
        else : pass

    return True

def solution(answers):
    length = len(answers)

    nums = list(answers)

    count = 0

    num_list = list(set(map(int, nums)))
    prime_list = []

    for num in num_list:
        if num in [0,1] : pass

        elif isprime(num) == True:
            count += 1
            prime_list.append(num)

    for i in range(length - 1):

        permuts = list(permutations(nums, i + 2))

        for i, permut in enumerate(permuts):
            permut_list = list(permut)
            joined_permut_list = "".join(permut_list)

            if int(joined_permut_list) in num_list : pass

            elif isprime(int(joined_permut_list)) == True:
                num_list.append(int(joined_permut_list))
                prime_list.append(int(joined_permut_list))
                count += 1

            else : num_list.append(int(joined_permut_list))

    print(num_list)
    print(prime_list)

    return count

print(solution("222"))


