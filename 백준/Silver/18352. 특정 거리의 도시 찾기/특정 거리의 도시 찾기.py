import sys
input = sys.stdin.readline

from heapq import heappush, heappop
N, M, K, X = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

graph = [[] for _ in range(N+1)]
INF = float("inf")
distance = [INF] * (N+1)
answer = []

def dijkstra(node):
    distance[node] = 0
    heap = [(0, node)] # 처음 힙 세팅

    while heap:
        
        min_dist, node = heappop(heap)
    
        if min_dist > distance[node]:
            continue

        for next_node, dist in graph[node]:
            next_dist = min_dist + dist
            if distance[next_node] > next_dist:
                distance[next_node] = next_dist
                heappush(heap, (next_dist, next_node))


for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append((B, 1))

dijkstra(X) # X로부터 출발하여 도달할 수 있는 도시 중에서
for i in range(len(distance)):
    if distance[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for city in answer:
        print(city, end= "\n")
 # 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력