def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, a, b, visited):
        visited[node] = True
        count = 1
        
        for nxt in graph[node]:
            if (node == a and nxt == b) or (node == b and nxt == a):
                continue
            
            if not visited[nxt]:
                count += dfs(nxt, a, b, visited)
        return count

    answer = float('inf')

    for a, b in wires:
        visited = [False] * (n+1)
        count = dfs(a, a, b, visited)
        diff = abs((n - count) - count)
        answer = min(answer, diff)

    return answer