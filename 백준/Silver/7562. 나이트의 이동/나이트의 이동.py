from collections import deque

T = int(input())

def solution(n, start, dest, board):
    

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1] 

    answer = 0
    
    def bfs():
        queue = deque()
        queue.append((start[0], start[1]))
        board[start[0]][start[1]] = 1

        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < n and 0<= ny < n and board[nx][ny] == 0:
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))
                    
    bfs()
  
    answer = board[dest[0]][dest[1]] - 1
    
    return answer

for _ in range(T):
   n = int(input())
   start = list(map(int, input().split()))
   dest = list(map(int, input().split()))
   board = [[0]*(n) for _ in range(n)]
   print(solution(n, start, dest, board))
   





