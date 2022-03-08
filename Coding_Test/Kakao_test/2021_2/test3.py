
def solution(n, k, cmd) :


    list = ['O'] * n

    list_dic = [[i, x] for i,x in enumerate(list)]
    ## [[0, 'O'], [1, 'O'], [2, 'O'], [3, 'O'], [4, 'O'], [5, 'O'], [6, 'O'], [7, 'O']]

    del_order = []
    ## 여기 남아있는 순서만 X로 바꿔주면된다.



    ## 현재위치를 계속 변경해야 한다.

    for order in cmd:

        if order[0] == 'D':
            k += int(order[2])

        elif order[0] == 'U':
            k -= int(order[2])

        elif order[0] == 'C':
            del_order.append(list_dic[k][0])
            del list_dic[k]
            if len(list_dic) == k :
                k -= 1
            else : pass

        elif order[0] == 'Z':
            list_dic.append([del_order[-1],'O'])
            list_dic.sort()
            del_order.pop()
            if k < del_order[-1]:
                pass
            else:
                k += 1

    for i in del_order :
        list[i] = 'X'

    return (''.join(list))

print(solution(8,2,	["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
