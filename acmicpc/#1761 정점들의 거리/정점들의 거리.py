import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
tree = [[] for _ in range(N+1)]
dist = [0] * (N+1)
parent = [[-1] * 20 for _ in range(N+1)]
depth = [-1] * (N+1)

for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

def dfs(v, d):
    depth[v] = d
    for next_v, w in tree[v]:
        if depth[next_v] == -1:
            dist[next_v] = dist[v] + w
            parent[next_v][0] = v
            dfs(next_v, d+1)

def set_parent():
    dfs(1, 0)
    for j in range(1, 20):
        for i in range(1, N+1):
            if parent[i][j-1] != -1:
                parent[i][j] = parent[parent[i][j-1]][j-1]

set_parent()

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    for i in range(19, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(19, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    ancestor = lca(a, b)
    print(dist[a] + dist[b] - 2 * dist[ancestor])
