from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

INF = int(1e9)

problem = 1

while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = cave[0][0]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                new_cost = dist[x][y] + cave[nx][ny]

                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    q.append((nx, ny))

    print(f"Problem {problem}: {dist[N-1][N-1]}")
    problem += 1