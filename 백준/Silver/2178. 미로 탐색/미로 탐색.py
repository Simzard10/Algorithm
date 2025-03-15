from collections import deque

N, M = map(int, input().split())

maze = []
for i in range(N):
    maze.append(list(map(int, input())))

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0 ,0]
    queue = deque()

    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and maze[nx][ny] != 0:
                maze[nx][ny] = maze[x][y] + 1 
                queue.append((nx, ny))

bfs()    

print(maze[N-1][M-1])
