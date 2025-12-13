# 단지별 dfs의 횟수 + 총 dfs 횟수(단지 갯수)
# 입력 받기 & 단지 셋팅
N = int(input())
apart = []
for i in range(N):
    apart.append(list(map(int, input())))
    
# 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(a, b):
    global count
    count +=1
    apart[a][b] = 0 # 방문 처리
    
    for i in range(4):
        ax = a + dx[i]
        by = b + dy[i]
        if 0<= ax < N and 0<= by < N and apart[ax][by] == 1:
            dfs(ax, by)

apart_num = []

for i in range(N):
    for j in range(N):
        if apart[i][j] ==1:
            count = 0 
            dfs(i, j)
            apart_num.append(count)
apart_num.sort()
print(len(apart_num))
for k in apart_num:
    print(k)