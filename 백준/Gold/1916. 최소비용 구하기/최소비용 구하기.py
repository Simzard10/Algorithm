from heapq import heappop, heappush

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수 
graph = [[] for _ in range(N+1)]
INF = float("inf")
distance = [INF] * (N+1) 

def dijkstra(node):
    distance[node] = 0
    heap = [(0, node)]

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
    x, y, w = map(int, input().split())
    graph[x].append((y, w))
start, end = map(int, input().split())
dijkstra(start)


print(distance[end])