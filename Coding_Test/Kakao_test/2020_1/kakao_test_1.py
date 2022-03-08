
def distance(a,b) :
    if a == 2 :
        if b in (1,3,5) :
            dis = 1
        elif b in (4,6,8) :
            dis = 2
        elif b in (7,9,0) :
            dis = 3
        elif b in ("#","*") :
            dis = 4
        elif b == a :
            dis = 0
    elif a == 5 :
        if b in (4,6,2,8) :
            dis = 1
        elif b in (1,3,0,7,9) :
            dis = 2
        elif b in ("#","*") :
            dis = 3
        elif b == a:
            dis = 0
    elif a == 8 :
        if b in (7,9,5,0) :
            dis = 1
        elif b in (4,6,2,"#","*") :
            dis = 2
        elif b in (1,3) :
            dis = 3
        elif b == a :
            dis = 0
    elif a == 0 :
        if b in ("#","*",8) :
            dis = 1
        elif b in (7,9,5) :
            dis = 2
        elif b in (4,6,2) :
            dis = 3
        elif b in (1,3) :
            dis = 4
        elif b == a :
            dis = 0

    return dis

################################################################################거리함수 정의

def solution(numbers,hand) :

    result = []

    left = "#"
    right = "*"

    for n in numbers:
        if n in (1,4,7):
            left = int(n)
            result.append("L")
        elif n in (3,6,9):
            right = int(n)
            result.append("R")
        elif n in (0,2,5,8) :
            if distance(n,left) < distance(n,right) :
                left = n
                result.append("L")
            elif distance(n,left) > distance(n,right) :
                right = n
                result.append("R")
            else :
                if hand == "right" :
                    right = n
                    result.append("R")
                elif hand == "left" :
                    left = n
                    result.append("L")

    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "left"))

#거리가 0인경우에 대해서 고려를 안해서 left를 했을때 오류가 발생함.-> 거리 0인경우도 추가

#함수를 좀더 간단하게 표현할 수 있는 방법에 대해서 생각해보자.