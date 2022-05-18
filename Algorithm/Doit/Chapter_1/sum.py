# 실습 1-9: a부터 b까지 정수의 합을 구하기(for문)

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요.: '))

if a > b:
    a, b = b, a  # a와 b를 오름차순으로 정렬

sum = 0
for i in range(a, b + 1):  # 뒤의 범위 미만의 수열을 만든다.
    sum += i

print(f'{a}부터 {b}까지 정수의 합은 {sum}입니다.')