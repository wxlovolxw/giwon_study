
import re

def check(list,operator) :
    operator_loc = []

    if operator == "plus":
        for n,con in enumerate(list) :
            if con == "+" :
                operator_loc.append(n)
    elif operator == "minus":
        for n,con in enumerate(list) :
            if con == "-" :
                operator_loc.append(n)
    elif operator == "mul":
        for n,con in enumerate(list) :
            if con == "*" :
                operator_loc.append(n)

    return operator_loc

###################################리스트내에 연산자 위치 찾기

def Cal_Plus(a) :  ##더하기
    plus_count = 0

    for n,con in enumerate(a) :
        if con == "+":
            plus_count += 1

    while plus_count > 0 :
        order = check(a,"plus")
        plus_result = str(int(a[order[0]-1])+int(a[order[0]+1]))

        if order[0] == 1:
            a = a[2:]
            a[0] = plus_result
        elif order[0]+1 == len(a)-1:
            a = a[:len(a)-2]
            a[len(a)-3] = plus_result
        else :
            a = a[:order[0]-1] + a[order[0]+1:]
            a[order[0]-1] = plus_result

        plus_count -= 1

    return a

def Cal_Minus(a) :      ## 빼기
    minus_count = 0

    for n,con in enumerate(a) :
        if con == "-":
            minus_count += 1

    while minus_count > 0 :
        order = check(a,"minus")
        minus_result = str(int(a[order[0]-1])-int(a[order[0]+1]))

        if order[0] == 1:
            a = a[2:]
            a[0] = minus_result
        elif order[0]+1 == len(a)-1:
            a = a[:len(a)-2]
            a[len(a)-3] = minus_result
        else :
            a = a[:order[0]-1] + a[order[0]+1:]
            a[order[0]-1] = minus_result

        minus_count -= 1

    return a

def Cal_Mul(a) :      ## 곱하기
    mul_count = 0

    for n,con in enumerate(a) :
        if con == "*":
            mul_count += 1

    while mul_count > 0 :
        order = check(a,"mul")
        mul_result = str(int(a[order[0]-1])*int(a[order[0]+1]))

        if order[0] == 1:
            a = a[2:]
            a[0] = mul_result
        elif order[0]+1 == len(a)-1:
            a = a[:len(a)-2]
            a[len(a)-3] = mul_result
        else :
            a = a[:order[0]-1] + a[order[0]+1:]
            a[order[0]-1] = mul_result

        mul_count -= 1

    return a


def solution(a) :

    list = re.findall("\d+|\D+", a)

    result = []

    result.append(abs(int(Cal_Minus(Cal_Plus(Cal_Mul(list)))[0])))
    result.append(abs(int(Cal_Minus(Cal_Mul(Cal_Plus(list)))[0])))
    result.append(abs(int(Cal_Plus(Cal_Minus(Cal_Mul(list)))[0])))
    result.append(abs(int(Cal_Plus(Cal_Mul(Cal_Minus(list)))[0])))
    result.append(abs(int(Cal_Mul(Cal_Plus(Cal_Minus(list)))[0])))
    result.append(abs(int(Cal_Mul(Cal_Minus(Cal_Plus(list)))[0])))

    result.sort(reverse=True)

    return result[0]

print(solution("100-200*300-500+20+500-291*12312"))
