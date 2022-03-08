import heapq as hq

def solution(scoville, K):

    scoville_small = [x for x in scoville if x < K]
    hq.heapify(scoville_small)

    if scoville_small == [] : return 0
    else :
        count = 0
        while len(scoville_small) > 1 :
            count += 1
            a = scoville_small[0]
            hq.heappop(scoville_small)
            b = scoville_small[0]
            hq.heappop(scoville_small)
            hq.heappush(scoville_small, a+2*b)

            if scoville_small[0] >= K :
                return count
            elif count > len(scoville) : break

        return -1




print(solution([1, 2, 3, 9, 10, 12], 7))