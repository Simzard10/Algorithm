import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split()) # 점의 개수를 나타내는 정수 n, 진행된 차례의 수를 나타내는 정수 m
parent = list(range(n))
rank = [0] * (n)
count = 0

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return False

    if rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    elif rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    else: # rank[x_root] == rank[y_root]
        parent[x_root] = y_root
        rank[y_root] += 1  

    return True
answer = 0 
for t in range(1, m+1):
    a, b = (map(int, input().split()))
    if not union(a, b):
        print(t)
        break
else:
    print(0)