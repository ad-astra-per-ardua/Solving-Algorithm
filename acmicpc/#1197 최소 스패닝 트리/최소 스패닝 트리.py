import sys
input = sys.stdin.readline

def find(u):
    if u != p[u]:
        p[u] = find(p[u])
    return p[u]

def union(u, v):
    root_u, root_v = find(u), find(v)
    if root_u != root_v:
        p[root_v] = root_u

v, e = map(int, input().split())
edges = []
p = [x for x in range(v+1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()
total_w = 0
for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        total_w += w

print(total_w)
