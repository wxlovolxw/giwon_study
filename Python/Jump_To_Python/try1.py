
list = [[0, 0, 0, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 0]]

def Possible_direction (current_x, current_y):

    current_location = list[current_y][current_x] # 필요 없을지도..

    possible_xy = []

    #모서리인 경우를 가장 먼저 따져야 하는가?

    if current_x == 0 and current_y == 0: #출발점에 있는 경우
        if list[0][1] == 0:
            possible_xy.append([1, 0])

        if list[1][0] == 0:
            possible_xy.append([0, 1])

        else: pass

    elif current_x == 0 and current_y == len(list)-1 : #왼쪽 아래 꼭지점에 있는 경우
        if list[len(list)-2][0] == 0:
            possible_xy.append([0, len(list) - 2])

        if list[len(list)-1][1] == 0:
            possible_xy.append([1, len(list) - 1])

        else: pass

    elif current_x == len(list)-1 and current_y == 0 :  #오른쪽 위 꼭지점에 있는 경우
        if list[0][len(list)-2] == 0:
            possible_xy.append([len(list)-2,0])

        if list[1][len(list)-1] == 0:
            possible_xy.append([len(list)-1,1])

    elif current_x == 0 :   #왼쪽 모서리에 있는 경우
        if list[current_y+1][0] == 0:
            possible_xy.append([0,current_y+1])
        if list[current_y-1][0] == 0:
            possible_xy.append([0,current_y-1])
        if list[current_y][1] == 0:
            possible_xy.append([1,current_y])

    elif current_y == 0 :   #위쪽 모서리에 있는 경우
        if list[0][current_x+1] == 0:
            possible_xy.append([current_x+1,0])
        if list[0][current_x-1] == 0:
            possible_xy.append([current_x-1,0])
        if list[1][current_x] == 0:
            possible_xy.append([current_x,1])

    elif current_x == len(list)-1 : #오른쪽 모서리에 있는 경우
        if list[current_y+1][current_x] == 0:
            possible_xy.append([current_x,current_y+1])
        if list[current_y-1][current_x] == 0:
            possible_xy.append([current_x,current_y-1])
        if list[current_y][current_x-1] == 0:
            possible_xy.append([current_x-1,current_y])

    elif current_y == len(list)-1 : #아래쪽 모서리에 있는 경우
        if list[current_y][current_x+1] == 0:
            possible_xy.append([current_x+1,current_y])
        if list[current_y][current_x-1] == 0:
            possible_xy.append([current_x-1,current_y])
        if list[current_y-1][current_x] == 0:
            possible_xy.append([current_x,current_y-1])

    else :  #모서리가 아닌경우는 모든 방향에 대해서.
        if list[current_y+1][current_x] == 0:
            possible_xy.append([current_x,current_y+1])
        if list[current_y-1][current_x] == 0:
            possible_xy.append([current_x, current_y-1])
        if list[current_y][current_x+1] == 0:
            possible_xy.append([current_x+1,current_y])
        if list[current_y][current_x-1] == 0:
            possible_xy.append([current_x-1,current_y])

    return possible_xy


def Shift(current_x,current_y) :
    list = Possible_direction(current_x,current_y)

    prior_x = current_x
    prior_y = current_y

    for factor in list :

        x = factor[0]
        y = factor[1]

        current_x = factor[0]
        current_y = factor[1]

        if current_x == prior_x :
            current_direction = "x"
        elif current_y == prior_y :
            current_direction = "y"

        print("prior location :", [prior_x, prior_y])
        print("current location :", [current_x,current_y])
        print("current direction :", current_direction)






print(Shift(0,0))

