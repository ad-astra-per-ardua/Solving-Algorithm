import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def solve():
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    count = 1
    def dfs(v):
        nonlocal count
        visited[v] = count
        graph[v].sort()
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                dfs(g)
    dfs(r)
    for i in range(1, n + 1):
        print(visited[i])
solve()