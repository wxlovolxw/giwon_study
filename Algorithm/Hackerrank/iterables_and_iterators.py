import sys

def factorial(num) :

    result = 1
    while num >= 1 :
        result *= num
        num -= 1

    return result

def combination(n, r) :
    result = int(factorial(n) / (factorial(n-r) * factorial(r)))

    return result

def find_a(list) :
    count = 0
    for i, word in enumerate(list) :
        if word == "a" :
            count += 1
        else : pass

    return count

def probability(count_num, words, com_num) :

    count_x = find_a(words)

    if count_num == count_x :
        result = 1/1
    else :
        result = 1 - (combination((count_num-count_x),com_num) / combination(count_num,com_num))

    return result

count_num = int(input())
words = input()
com_num = int(input())

print(probability(count_num, words, com_num))