import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from bisect import bisect_left, bisect_right
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_000
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########
pop = hq.heappop
push = hq.heappush

def ip(): return int(input())
def sp(): return str(input().rstrip())
def mip(): return map(int, input().split())
def msp(): return map(str, input().split().rstrip())
def lmip(): return list(map(int, input().split()))

def lmsp(): return list(map(str, input().split()))


sys.setrecursionlimit(100000)

L = [0 for _ in range(404040)]
R = [0 for _ in range(404040)]
g = [[] for _ in range(404040)]
seg = [0 for _ in range(404040)]
lazy = [0 for _ in range(404040)]

c = 0


def dfs(x, p):
    global c
    c += 1
    L[x] = c
    for i in g[x]:
        if i != p:
            dfs(i, x)
    R[x] = c


def lazyProp(x, s, e):
    if lazy[x] == 0:
        return
    seg[x] += (e - s + 1) * lazy[x]
    if s != e:
        lazy[x * 2] += lazy[x]
        lazy[x * 2 + 1] += lazy[x]
    lazy[x] = 0


def update(x, s, e, l, r, k):
    lazyProp(x, s, e)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg[x] += (e - s + 1) * k
        if s != e:
            lazy[x * 2] += k
            lazy[x * 2 + 1] += k
        return
    m = (s + e) // 2
    update(x * 2, s, m, l, r, k)
    update(x * 2 + 1, m + 1, e, l, r, k)
    seg[x] = seg[x * 2] + seg[x * 2 + 1]


def getSum(x, s, e, l, r):
    lazyProp(x, s, e)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg[x]
    m = (s + e) // 2
    return getSum(x * 2, s, m, l, r) + getSum(x * 2 + 1, m + 1, e, l, r)


N, M = mip()
a = lmip()
for i in range(N):
    if a[i] == -1:
        continue
    g[i + 1].append(a[i])
    g[a[i]].append(i + 1)

dfs(1, -1)

for Q in range(M):
    q = lmip()
    if q[0] == 1:
        update(1, 1, N, L[q[1]], R[q[1]], q[2])
    else:
        print(getSum(1, 1, N, L[q[1]], L[q[1]]))