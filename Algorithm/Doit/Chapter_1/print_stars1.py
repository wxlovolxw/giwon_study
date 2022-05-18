# 실습 1-14: *를 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

for i in range(n):
    print('*', end='')
    if i % w == w - 1:
        print()  # i가 w로 나눈 값이 w-1이 될 때 마다 줄바꿈을 한다.

if n % w:
    print()  # n이 w의 배수가 아니면 줄바꿈을 for문 밖에서 따로 해줘야 한다.