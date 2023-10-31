import math,sys
import heapq as hq
from itertools import permutations, combinations, combinations_with_replacement
from sys import stdin, stdout,setrecursionlimit
from math import gcd, floor, sqrt, log, factorial
from bisect import bisect_left as bl, bisect_right as br
def lcm(x, y):
    return x * y // gcd(x, y)
def perm(n, r):
    return math.factorial(n) // math.factorial(n-r)
def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
def ceil(x):
    return int(x) if (x == int(x)) else int(x) + 1
def ceildiv(x, d):
    return x // d if (x % d == 0) else x // d + 1
def stdstr():
    return stdin.readline()

# MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdstr().strip()
######### main code goes here #########

from collections import defaultdict

MAX = 51
INF = 9999

# Tarjan's algorithm
graph = defaultdict(list)
id = [0] * MAX
SCC = []
visited = [False] * MAX
S = []
cnt = 0

def dfs(cur):
    global cnt
    visited[cur] = True
    ret = id[cur] = cnt + 1
    cnt += 1
    S.append(cur)
    for nxt in graph[cur]:
        if not id[nxt]:
            ret = min(ret, dfs(nxt))
        elif visited[nxt]:
            ret = min(ret, id[nxt])
    if ret == id[cur]:
        scc = []
        while True:
            t = S.pop()
            scc.append(t)
            visited[t] = False
            id[t] = MAX
            if t == cur:
                break
        SCC.append(scc)
    return ret

N = int(input())
price = list(map(int, input().split()))

for i in range(N):
    s = input().strip()
    for j, char in enumerate(s):
        if char == 'Y':
            graph[i].append(j)

# find SCC
for i in range(N):
    if not id[i]:
        dfs(i)

# find minimum cost for SCCs with no incoming edges
ans = 0
iter = 0
while SCC:
    scc = SCC.pop()

    # find incoming edges
    in_flag = False
    for u in range(N):
        if u in scc:
            continue
        for v in graph[u]:
            if v in scc:
                in_flag = True
                break
        if in_flag:
            break
    if in_flag:
        continue

    # find minimum cost
    mc = INF
    mi = -1
    for u in scc:
        if price[u] < mc:
            mc = price[u]
            mi = u
    ans += mc
    price[mi] = INF
    iter += 1

# update average
price.sort()
for p in price:
    if ans > p * iter:
        ans += p
        iter += 1
    else:
        break
print("{:.15f}".format(ans / iter))
