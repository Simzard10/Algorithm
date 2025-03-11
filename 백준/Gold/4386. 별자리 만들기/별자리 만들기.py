import sys
import math
sys.setrecursionlimit(10000000)  
input = sys.stdin.readline

n = int(input())

parent = list(range(n+1))
rank = [0] * (n+1)
edges = []
total = 0
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return True
    
    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[y_root] < rank[x_root]:
        parent[x_root] = y_root
    else:
        parent[x_root] = y_root
        rank[y_root] += 1

    return False

stars = []
for i in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge
    if not union(x, y):
        total += cost

print(round(total, 2))
