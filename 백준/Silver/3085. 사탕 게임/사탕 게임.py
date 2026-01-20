N = int(input())
board = [list(input()) for _ in range(N)]

def check(board):
    max_cnt = 1

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt

answer = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < N and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, check(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(answer)