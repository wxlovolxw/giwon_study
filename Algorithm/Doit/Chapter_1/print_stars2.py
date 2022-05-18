# 실습 1-15: *를 출력하되 w개마다 줄바꿈하기 2

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for _ in range(n // w):
    print('*' * w)

rest = n % w  # n을 w로 나눈 값이 0이 아니라면 그만큼 *를 출력한다.
if rest:
    print('*' * rest)