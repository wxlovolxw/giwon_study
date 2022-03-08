import heapq as hq

def solution(operations) :

    a_list = list(map(lambda x : [str(list(x)[0]),int("".join(list(x)[2:]))], operations))
    heap = []

    for i in a_list :
        if i[0] == 'I' :
            hq.heappush(heap, i[1])
        elif heap == [] : pass
        elif i == ['D', 1] :
            heap = list(map(lambda x : -x, heap))
            hq.heapify(heap)
            hq.heappop(heap)
            heap = list(map(lambda x: -x, heap))
            hq.heapify(heap)
        elif i == ['D', -1] :
            hq.heapify(heap)
            hq.heappop(heap)

    if heap == [] : return [0,0]
    else : return [max(heap), min(heap)]


print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

