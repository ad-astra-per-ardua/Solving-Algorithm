import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_000
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########
from collections import defaultdict

def dfs(u, e, c):
    if u == e:
        return True
    visited[u] = c
    for v in adj[u]:
        if adj[u][v] == 0 or visited[v] == c:
            continue
        if dfs(v, e, c):
            adj[u][v] -= 1
            adj[v][u] += 1
            return True
    return False

n, k, d = map(int, input().split())
adj = [defaultdict(int) for _ in range(n + d + 2)]
visited = [-1] * (n + d + 2)

for i in range(1, n + 1):
    adj[0][i] = k
    adj[i][0] = 0

capacity = list(map(int, input().split()))
for i, s in enumerate(capacity, start=1):
    adj[n + i][n + d + 1] = s
    adj[n + d + 1][n + i] = 0

for i in range(1, n + 1):
    _, *neighbors = map(int, input().split())
    for t in neighbors:
        adj[i][n + t] = 1
        adj[n + t][i] = 0

ans = 0
while dfs(0, n + d + 1, ans + 1):
    ans += 1

print(ans)
