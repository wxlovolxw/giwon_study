
# [식 for 변수 in 리스트]
# list( 식 for 변수 in 리스트)

# 성능은 위의 대괄호 방식이 더 좋다. 아래방식은 C언어 스타일.

a = [i for i in range(10)]

b = list(i for i in range(10))

c = [i+5 for i in range(10)]

d = [i*2 for i in range(10)]

# [식 for 변수 in 리스트 if 조건식]

e = [i for i in range(10) if i % 2 == 0]

f = [i+5 for i in range(10) if i % 2 == 1]

# [식 for 변수1 in 리스트1 if 조건식1 for 변수2 in 리스트2 if 조건식2 ...]

g = [i*j for j in range(2,10) for i in range(1,10)]

g = [i*j for j in range(2,10)
        for i in range(1,10)]   #고독성을 위해 줄을 띄우는 것이 좋다.

#조건식이 2개인 경우, 뒷 조건식의 i가 먼저 처리되고 j가 처리된다.