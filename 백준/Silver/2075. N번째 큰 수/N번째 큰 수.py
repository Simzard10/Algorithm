import heapq

N = int(input())

heap = []

for _ in range(N):
    temp = list(map(int, input().split()))
    for j in temp:
        if len(heap) < N:
            heapq.heappush(heap, j)
        else:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap, j)

print(heap[0])
