import sys
from collections import deque
input = sys.stdin.readline


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = -visited[v]
                queue.append(i)
            elif visited[i] == visited[v]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]
    bg = True

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(i):
                bg = False
                break

    print('YES' if bg else 'NO')
