from collections import deque

N = int(input()) # 공간의 크기
# 공간 구성
space = [] 
for i in range(N):
    space.append(list(map(int, input().split())))

start_x, start_y = 0, 0 # 아기 상어 현재 좌표

# 우선 아기 상어가 있는 위치부터 확인
for i in range(N):
      for j in range(N):
            if space[i][j] == 9:
                  space[i][j] = 0
                  start_x, start_y = i, j

INF = 10000000000000 # 최단 거리 구하기 위한 값
shark_size = 2 # 아기 상어 초기 크기

# 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((start_x, start_y))
    visited = [[-1]*N for _ in range(N)] # 방문 여부 (거리 계산)
    visited[start_x][start_y] = 0
   
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx <N and 0 <= ny < N:
                if shark_size >= space[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited

def solve(visited):
    x, y = 0, 0
    min_distance = INF
    for i in range(N):
         for j in range(N):
            if visited[i][j] != -1 and 1 <= space[i][j] < shark_size:
                 if visited[i][j] < min_distance:
                      min_distance = visited[i][j]
                      x, y = i, j
    if min_distance==INF:
        return False
    else: 
        return x, y, min_distance
    
answer = 0
food = 0

while(True): # 엄마 부를 때 까지 계속
    result = solve(bfs())

    if result == False:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        space[now_x][now_y] = 0
        food += 1
        start_x, start_y = now_x, now_y
    
    if food >= shark_size:
        shark_size +=1
        food = 0