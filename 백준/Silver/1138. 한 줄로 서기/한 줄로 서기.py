import sys

n = int(sys.stdin.readline())
left_counts = list(map(int, sys.stdin.readline().split()))
result = [0] * n

for i in range(n):
    count = left_counts[i]
    for j in range(n):
        if count == 0 and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            count -= 1

print(*(result))