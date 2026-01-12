import sys
sys.setrecursionlimit(100000)

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = []

def dfs(x, y, field, M, N):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and field[nx][ny] != 0:
            field[nx][ny] = 0
            dfs(nx , ny, field, M, N)
    return

for _ in range(T):
    count = 0
    M, N, K = map(int, input().split())
    field = []
    for _ in range(M):
        arr = [0] * N
        field.append(arr)

    for _ in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1
    
    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                count +=1
                field[i][j] = 0
                dfs(i, j, field, M, N)
        
    result.append(count)
for count in result:
    print(count)