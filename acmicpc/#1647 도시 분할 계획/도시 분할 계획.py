import sys
input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

n, m = map(int, input().split())
edges = []
parent = list(range(n + 1))

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

total = 0
max_edge = 0

for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        total += cost
        max_edge = cost

print(total - max_edge)
