import sys
input = sys.stdin.readline

from heapq import heappush, heappop

n, m, r = map(int, input().split()) # 지역의 개수, 수색 범위, 길의 개수
items = list(map(int, input().split())) # 아이템의 수
graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    

INF = float("inf")

def dijkstra(node):
    distance[node] = 0
    heap = [(0, node)]

    while heap:
        dist, node = heappop(heap)
        if distance[node] < dist:
            continue

        for next_node, dist in graph[node]:
            min_dist = distance[node] + dist
            if distance[next_node] > min_dist:
                distance[next_node] = min_dist
                heappush(heap, (min_dist, next_node))

answer = 0
for i in range(1, n+1): # 각 지역 마다 다익스트라
    distance = [INF] * (n+1)
    dijkstra(i)
    temp = 0
    for j in range(1, len(distance)):
        if distance[j] <= m:
            temp += items[j-1]
    if temp >= answer:
        answer = temp

print(answer)