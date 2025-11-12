from heapq import heappop, heappush

def solution(scoville, K):
    heap = []
    count = 0
    for i in range(len(scoville)):
        heappush(heap, scoville[i])
    while(1):
        if len(heap)<=1 and heap[0] < K:
            count = -1
            break
        if heap[0] >= K:
            break

        min_scovile = heappop(heap)
        second_minscovile = heappop(heap)

        new_scovile = min_scovile + (second_minscovile*2)
        heappush(heap, new_scovile)
        count +=1

    return count