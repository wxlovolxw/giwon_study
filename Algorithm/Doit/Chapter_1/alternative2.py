# 실습 1-13: +와 -를 번갈아 출력하기2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))

for _ in range(n // 2):
    print('+-', end='')  # +-를 n//2개 출력한다.

if n % 2:
    print('+', end='')  # 나머지가 1이면 +를 한번 출력, 아니라면 출력하지 않는다.

# else : pass

print()