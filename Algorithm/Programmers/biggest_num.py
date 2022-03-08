def solution(numbers):

    num_list = list(map(lambda x: ["".join(list(str(x) * 4)[:4]), x], numbers))

    sol = "".join(list(map(lambda x: str(x[1]), sorted(num_list,reverse=True))))

    if list(sol)[0] == '0' :
        return "0"
    else : return sol

print(solution([0,0,0,0,0]))