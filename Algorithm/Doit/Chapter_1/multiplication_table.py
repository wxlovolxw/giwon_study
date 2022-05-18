#실습 1-21: 구구단 곱셈표 출력하기

print('-'*27)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:3}',end='') #f를 통한 문자열 포맷팅 시에 :뒤의 숫자를 통해 몇자리 까지 표현할껀지 지정
    print()
print('-'*27)