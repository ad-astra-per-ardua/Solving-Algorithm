import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

maxn = int(2e5 + 5)
graph = [[] for _ in range(maxn)]


def dfs(u: int) -> int:
    if len(graph[u]) == 0:
        return 1
    chv = []
    for v in graph[u]:
        chv.append(dfs(v))
    if len(chv) == 1:
        return chv[0]
    chv.sort()
    return max(1 + chv[-2], chv[-1])


def solve():
    n = int(input())
    for i in range(n):
        graph[i].clear()
    p_values = list(map(int, input().split()))
    for i in range(1, n):
        p = p_values[i] - 1
        graph[p].append(i)
    print(dfs(0))


tcs = int(input())
for _ in range(tcs):
    solve()
