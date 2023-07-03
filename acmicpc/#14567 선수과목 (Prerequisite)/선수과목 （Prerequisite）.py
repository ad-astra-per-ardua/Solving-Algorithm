import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
semester = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1


def topology_sort():
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            semester[i] = 1
    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            semester[i] = max(semester[i], semester[now] + 1)
            if indegree[i] == 0:
                q.append(i)


topology_sort()
print(' '.join(map(str, semester[1:])))
