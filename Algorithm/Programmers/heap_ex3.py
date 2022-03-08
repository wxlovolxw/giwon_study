import heapq as hq
import math

def solution(jobs) :

    result_list = [] # 요청부터 완료시간을 넣기 위한 리스트

    count = 0 # count를 0으로 초기화

    while True : # 반복문

        if jobs == [] : break   # 더이상 연산할 리스트가 남아있지 않다면 break를 통해 빠져나온다.

        jobs_small = [x for x in jobs if x[0] <= count] #count보다 작은 요청시간에 대해서 진행해야 하므로, jobs를 두개의 리스트로 나눠주었다.
        jobs_big = [x for x in jobs if x[0] > count]

        if jobs_small != [] :
            jobs_small = list(map(lambda x : [x[1],x[0]], jobs_small))
            hq.heapify(jobs_small)
            next_job = hq.heappop(jobs_small)   # small중에
            result_list.append(count+next_job[0]-next_job[1])
            count += next_job[0]
            jobs_small = list(map(lambda x : [x[1],x[0]], jobs_small))

        else :  # jobs_small이 비었다면 요청시간이 가장 작은 작업을 시행해야 하므로,
            hq.heapify(jobs_big)
            next_job = hq.heappop(jobs_big)
            result_list.append(next_job[1])
            count = next_job[0]+next_job[1]

        jobs = jobs_small + jobs_big

    if result_list == [] : return 0
    else : return math.trunc(sum(result_list)/len(result_list))

