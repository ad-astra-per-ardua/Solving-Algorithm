import sys,math,time
from itertools import permutations,combinations,combinations_with_replacement
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, perm, comb
from collections import defaultdict,deque
from bisect import bisect_left as bl, bisect_right as br
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
def flush(): return stdout.flush()
def stdstr(): return stdin.readline()

mod = 1_000_000_007
# sys.setrecursionlimit(100_000_000)
input = lambda: stdstr().strip()
# main code goes here

def process_bfs(graph, depths, visited, start, end, n):
    tracking = [0] * (n + 1)
    depths[start] = 0
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        for next in graph[curr]:
            if depths[next] == -1:
                depths[next] = depths[curr] + 1
                tracking[next] = curr
                queue.append(next)

    idx = end
    while idx != 0:
        visited[idx] = True
        idx = tracking[idx]


def main():
    n, m, s, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    edges = []
    depths = [-1] * (n + 1)
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))

    process_bfs(graph, depths, visited, s, e, n)

    if depths[e] == -1:
        print(-1)
        return

    result = []
    for u, v in edges:
        if visited[u] and visited[v]:
            result.append(str(1) if depths[u] >= depths[v] else str(0))
        elif visited[u]:
            result.append(str(1))
        elif visited[v]:
            result.append(str(0))
        else:
            result.append(str(0))

    print(" ".join(result))


if __name__ == "__main__":
    main()
