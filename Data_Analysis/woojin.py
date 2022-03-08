import scipy.integrate as spi # 수학적 계산을 위한 python 라이브러리
import numpy as np  # 일차원 행렬을 사용하기 위한 python 라이브러리
import matplotlib.pyplot as plt # 그래프를 그리기 위한 python 라이브러리

# 논문을 통해 beta와 gamma값을 인용. 보통 0.1-0.2 사이의 값을 사용
beta = 0.2
gamma = 1/14

# 약 2년의 시간을 1일 간격으로 확인해보고자 한다
t_start = 0
t_end = 700
t_inc = 1

N = 40000000    # 우리나라의 인구 약 4천만명
S0 = N-1   # 초기에는 모두 감염 대상군
I0 = 1   # 초기 감염자 수 0
R0 = 0   # 초기 회복자 수 0

S_rate = S0/N   # 전체 인원수에 대한 감염 대상군의 비율
I_rate = I0/N   # 전체 인원수에 대한 감염자의 비율
R_rate = R0/N   # 전체 이원수에 대한 회복자의 비율

Input  = (S_rate, I_rate, 0)    # 초기값으로는 한명의 감염자가 있다는 가정

def simple_SIR(INT, t): # SIR 함수의 정의. 초기값으로 두개의 변수를 받는다.

    Y = np.zeros((3))   # 세개의 값을 받는 빈 리스트를 생성
    Y[0] = -beta * INT[0] * INT[1]  # 첫번째 Y값은 시간에 대한 S의 변화
    Y[1] = beta * INT[0] * INT[1] - gamma * INT[1] # 두번째 Y값은 시간에 대한 I의 변화
    Y[2] = gamma * INT[1] # 세번째 값은 시간에 대한 R의 변화
    return Y    # 계산된 세 값을 저장한 Y를 반환한다.

t_range = np.arange(t_start, t_end+t_inc, t_inc)    # 시간의 범위는 우리가 설정한 0일부터 700일까지 하루 간격으로 관찰
SIR = spi.odeint(simple_SIR, Input, t_range)    # 미분방정식의 수치적분을 수행하는 함수
                                                # 첫 번째 변수인 simple_SIR은 함수의 형태가 들어오며
                                                # 두 번째 변수인 Input은 초기값, 마지막 변수는 시간이 들어오게 된다.

plt.figure(figsize=(8,8))                       # 그래프의 사이즈를 지정
plt.plot(t_range, SIR[:,0],'g', label = "S")    # SIR 그래프의 첫 번째 요소는 초록색 감염대상군의 수
plt.plot(t_range, SIR[:,1],'k', label = "I")    # 두 번째 요소는 검정색 감염자의 수
plt.plot(t_range, SIR[:,2],'r', label = "R")    # 세 번쨰 요소는 빨간색 회복자의 수

plt.title("Prediction of Simple COVID-19 SIR model")    # 그래프의 타이틀 입력
plt.xlabel("days")                                      # x축 타이틀 입력
plt.ylabel("number of people")                          # y축 타이틀 입력
plt.legend()

plt.show()                                              # 그래프 띄우기


