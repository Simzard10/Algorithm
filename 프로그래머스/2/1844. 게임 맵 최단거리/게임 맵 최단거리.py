import collections

def bfs(x, y, maps, queue): 
    n = len(maps)
    m = len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == (n-1, m-1):
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<= nx < n and 0<= ny < m and maps[nx][ny] == 1):
                maps[nx][ny] = 0
                queue.append((nx, ny, dist + 1))
    return -1
        

def solution(maps):
    queue = collections.deque([(0, 0, 1)])
    return bfs(0, 0, maps, queue)
