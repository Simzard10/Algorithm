from collections import deque

N, K = map(int, input().split())
durability = deque(map(int, input().split()))
robots = deque([0] * (2 * N))

step = 0

while True:
    step += 1

    durability.rotate(1)
    robots.rotate(1)

    robots[N-1] = 0

    for i in range(N-2, -1, -1):
        if robots[i] == 1 and robots[i+1] == 0 and durability[i+1] > 0:
            robots[i] = 0
            robots[i+1] = 1
            durability[i+1] -= 1

    robots[N-1] = 0

    if durability[0] > 0 and robots[0] == 0:
        robots[0] = 1
        durability[0] -= 1

    if durability.count(0) >= K:
        print(step)
        break