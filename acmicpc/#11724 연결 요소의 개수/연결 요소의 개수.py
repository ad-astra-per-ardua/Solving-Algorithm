import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if visited[e] == False:
            dfs(e)


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count =0

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        count += 1
print(count)