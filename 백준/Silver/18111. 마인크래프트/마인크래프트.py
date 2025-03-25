# from collections import Counter

# N, M, B = map(int, input().split())

# house = []

# for _ in range(N):
#     house.append(list(map(int, input().split())))

# num_count = [0 for _ in range(256)]

# a = Counter(num_count)
# print(a.most_common(1))

# for i in range(N):
#     for j in range(M):
#         num_count[house[i][j]] +=1 

# print(num_count.index(1))

N, M, B = map(int, input().split())

house = []

answer = []

min_time = float('inf')
answer_height = 0

for _ in range(N):
    house.append(list(map(int, input().split())))

for target_h in range(257): # 0부터 256까지 브루트포스
    total_time = 0
    inventory = B

    for i in range(N):
        for j in range(M):
            height = house[i][j]
            diff = height - target_h

            if diff > 0: # 블록 제거: 인벤토리 +1, 시간 +2초
                total_time += diff * 2
                inventory += diff
            elif diff < 0: # 블록 쌓기: 인벤토리 -1, 시간 +1
                total_time += -diff * 1
                inventory -= -diff
    if inventory >= 0:
        if total_time < min_time:
            min_time = total_time
            answer_height = target_h
        elif total_time == min_time:
            if target_h > answer_height:
                min_time = total_time
                answer_height = target_h

print(min_time, answer_height)