
n, m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1   # 카운트를 1로 초기화 하며 이동 횟수를 센다.
turn_time = 0 # 회전 횟수를 0으로 초기화

while True:
    # 위에서 정의한 함수를 이용하여 회전을 실행. 초기 방향은 입력값으로 받는다.
    turn_left() # 반시계로 돌기 실행 direction값 1 감소. -> 새로운 방향에 대해서
    nx = x + dx[direction]  # 새로 설정한 방향에 대해서 x방향으로 이동을 시킨다.
    ny = y + dy[direction]  # 마찬가지 방법으로 y로 이동

    if d[nx][ny] == 0 and array[nx][ny] == 0: # 만약 이동한 곳이 땅이면서 방문한 적이 없는 지역이라면,
        d[nx][ny] = 1 # 방문 지역으로 갱신
        x = nx
        y = ny  # 좌표의 이동
        count += 1 # 방문횟수로 갱신
        turn_time = 0 # 회전 횟수는 그대로 0
        continue

    else : # 회전한 이후에 가보지 않은 칸이 없거나, 바라보는 방향이 바다라면
        turn_time += 1

    if turn_time == 4: # 한바퀴 돌았음에도 이동할수 없는 칸이 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 이동가능할 시에 이동하기
        if array[nx][ny] == 0 :
            x = nx
            y = ny

        # 뒤가 바다로 막혀있는 경우
        else :
            break

        turn_time = 0

print(count)


