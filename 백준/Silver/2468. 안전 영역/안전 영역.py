import sys
sys.setrecursionlimit(10000000)  
input = sys.stdin.readline

N = int(input())

rain = []

for _ in range(N):
    rain_list = list(map(int, input().split()))
    rain.append(rain_list)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, height):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx < N and 0<= ny < N:
            if not visited[nx][ny] and rain[nx][ny] > height:
                visited[nx][ny] = True
                dfs(nx, ny, height)  

max_safe_zone = 0

for height in range(0, 101):  
    visited = [[False] * N for _ in range(N)]
    safe_zone_count = 0

    for i in range(N):
        for j in range(N):
            if rain[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, height)
                safe_zone_count += 1

    max_safe_zone = max(max_safe_zone, safe_zone_count)

print(max_safe_zone)