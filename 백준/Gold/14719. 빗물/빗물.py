H, W = map(int, input().split())
world = list(map(int, input().split()))

max_height = max(world)
max_height_idx = world.index(max_height)

count = 0

left_max = world[0]
for i in range(1, max_height_idx):
    left_max = max(left_max, world[i])
    count += max(0, left_max - world[i])

right_max = world[-1]
for i in range(W-2, max_height_idx, -1):
    right_max = max(right_max, world[i])
    count += max(0, right_max - world[i])

print(count)