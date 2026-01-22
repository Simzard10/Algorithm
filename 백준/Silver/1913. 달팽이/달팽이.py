N = int(input())
target = int(input())

board = [[0] * N for _ in range(N)]

x = y = N // 2
board[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 2
step = 1
dir_idx = 0

if target == 1:
    tx, ty = x + 1, y + 1
else:
    tx = ty = 0

while num <= N * N:
    for _ in range(2):
        for _ in range(step):
            if num > N * N:
                break

            x += dx[dir_idx]
            y += dy[dir_idx]
            board[x][y] = num

            if num == target:
                tx, ty = x + 1, y + 1

            num += 1

        dir_idx = (dir_idx + 1) % 4

    step += 1

for row in board:
    print(*row)
print(tx, ty)