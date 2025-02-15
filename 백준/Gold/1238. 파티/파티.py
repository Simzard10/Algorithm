from heapq import heappush, heappop

N, M, X = map(int, input().split())


edges = []
for i in range(M):
    edges.append(list(map(int, input().split())))
    
def solution(n, edges, X): 
    
    INF = float("inf")
    distance1 = [INF] *(n+1)
    distance2 = [INF] *(n+1)
    graph1 = [[] for _ in range(n+1)]
    graph2 = [[] for _ in range(n+1)]
    answer = 0
    def dijkstra(node, graph, distance):
        distance[node] = 0
        heap = [(0, node)]
        
        while heap:
            
            min_dist, node = heappop(heap)

            if distance[node] < min_dist:
                continue

            for next_node, dist in graph[node]:
                next_dist = dist + min_dist

                if distance[next_node] > next_dist:
                    distance[next_node] = next_dist
                    heappush(heap, (next_dist, next_node))
    
    for x, y, w in edges:
        graph1[x].append((y, w))
        graph2[y].append((x, w))

    dijkstra(X, graph1, distance1)
    dijkstra(X, graph2, distance2)
    
    for i in range(1, len(distance1)):
        answer = max(distance1[i] + distance2[i], answer)

    return answer

print(solution(N, edges, X))
