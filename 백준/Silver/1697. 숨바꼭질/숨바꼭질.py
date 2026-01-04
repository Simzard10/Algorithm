from collections import deque

N, K = map(int, input().split())
MAX = 1000001

visited = [0] * MAX
queue = deque()
visited[N] = 1
queue.append((N, 0))

def bfs():
    while(queue):
        x, count = queue.popleft()

        if x ==K:
            print(count)
            break

        for i in (x-1, x+1, x*2):
            if 0<= i < MAX and visited[i] == 0:
                visited[i] =1 
                queue.append((i, count +1))
bfs()
