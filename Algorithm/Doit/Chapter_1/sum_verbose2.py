# 실습 1-11: a부터 b까지 정수의 합을 구하기2

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b):  # 마지막 b값은 마지막에 따로 더해준다. if문을 최소화 하기 위해
    print(f'{i} + ', end='')
    sum += i

print(f'{b} = ', end='')
sum += b

print(sum)