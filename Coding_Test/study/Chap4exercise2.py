n, m = map(int, input().split()) # 첫 입력으로 n과 m을 받는다.

d = [[0]*m for _ in range(n)] # m * n 짜리 행렬을 생성, 모든 값을 0으로

x, y, direction = map(int, input().split()) # 첫좌표와 방향을 지정

d[x][y] = 1 # 첫 위치의 값을 0으로 바꾼다.

# 어차피 이동을 하면서 주변에 존재하는 0의 값을 카운트 하면서 이동해야 하므로, 방향 이동에 대해서 정의하고,
# 그에 따라 이동을 하면서 총 연결된 0의 갯수를 세어줘야 한다.

# 처음 위치에서 이동가능한 값들을 리스트에 저장한다.

count = 1 # count를 초기화

list = []
list.append((x,y))

for i in list:
    list_2 = []
    if d[x-1][y] == 0:
        count += 1
        list_2.append((x-1,y))
    elif d[x+1][y] == 0:
        count += 1
        list_2.append((x+1,y))
    elif d[x][y-1] == 0:
        count += 1
        list_2.append((x,y-1))
    elif d[x+1][y] == 0:
        count += 1
        list_2.append((x,y+1))