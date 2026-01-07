from collections import deque

n, m = map(int, input().split())

world = []

queue = deque()

distance = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(-1)
    distance.append(row)

for i in range(n):
    world.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if world[i][j] == 2:
            distance[i][j] = 0
            queue.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

count = 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if distance[nx][ny] == -1: 
                if world[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif world[nx][ny] == 0:
                    distance[nx][ny] = 0
        
        if 0 <= nx < n and 0 <= ny < m and world[nx][ny] == 1:
            world[nx][ny] = world[x][y] + 1 
            queue.append((nx, ny))
            
for i in range(n):
    for j in range(m):
        if world[i][j] == 0:
            distance[i][j] = 0

for row in distance:
    print(*(row))