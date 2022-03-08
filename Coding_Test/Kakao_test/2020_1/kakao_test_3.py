def check(a,b) :
    a.sort()
    b.sort()
    if a == b :
        return True

def solution(gems) :

    mo_gems = list(set(gems))

    result = []     #시작하는 포인트와 끝나는 포인트를 append해서 출력하기 위함.
    t = 0           #t값 초기화
    while len(mo_gems) + t <= len(gems) :

        for i, gem in enumerate(gems) :
            gems_check = list(set(gems[i:i+len(mo_gems)+t]))

				#i번째부터 i+len(mo_gems)+t

            if i + t > len(gems) :
                pass
            else :
                if check(mo_gems,gems_check) == True:
                    result.append(i+1)
                    result.append(i+len(mo_gems)+t)
                    break
                else : pass
        if result :
            break
        else :
            pass

        t += 1

    return result

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))