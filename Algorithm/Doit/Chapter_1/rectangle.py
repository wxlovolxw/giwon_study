#실습 1-17: 가로, 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area+1):
    if i * i > area : break # 만약 이 조건을 만족하면 i가 긴변이 되어버리기 때문에 break를 통해 종료
    if area % i : continue # i가 area의 약수가 되도록
    print(f'{i} * {area//i}')