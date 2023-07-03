import sys
from collections import deque

def solve():
    N, K = map(int, sys.stdin.readline().split())
    D = [0] + list(map(int, sys.stdin.readline().split()))
    build_order = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        build_order[X].append(Y)
        indegree[Y] += 1
    W = int(sys.stdin.readline())
    dp = [0] * (N+1)
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = D[i]

    while queue:
        now = queue.popleft()

        for i in build_order[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + D[i])
            if indegree[i] == 0:
                queue.append(i)

    print(dp[W])

T = int(sys.stdin.readline())
for _ in range(T):
    solve()
