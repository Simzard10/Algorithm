
V, E = map(int, input().split())


parent = list(range(V+1))
rank = [0] * (V+1)

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
    else: 
        parent[y_root] = x_root
        rank[x_root] += 1  # 같은 높이일 경우 한 쪽을 증가
    return True

edges =[]

for i in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
total = 0

for edge in edges:
    C, A, B = edge
    if union(A, B):
        total += C

print(total)