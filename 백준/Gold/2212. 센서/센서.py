import sys

N = int(input())
K = int(input())

sensors = list(map(int, input().split()))
sensors.sort()

if K >= N:
    print(0)
    exit()

distance = []

for i in range(1, len(sensors)):
    distance.append(sensors[i]-sensors[i-1])
distance.sort()

for _ in range(K-1):
    distance.pop()

print(sum(distance))