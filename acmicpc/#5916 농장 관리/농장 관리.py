import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from bisect import bisect_left, bisect_right
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_000
setrecursionlimit(10**5)
input = lambda: stdin.readline().strip()

######### main code goes here #########

import sys
from math import floor, log2

MAX = 100000
N, M = 0, 0
maxPower = floor(log2(MAX))
ac = [[0] * 21 for _ in range(MAX + 1)]
dpt = [0] * (MAX + 1)
adj = [[] for _ in range(MAX + 1)]
st = [0] * (MAX + 1)
ed = [0] * (MAX + 1)
tree = [0] * (MAX << 2)

num = 0


def dfs(now, parent):
    global num
    st[now] = num = num + 1
    dpt[now] = dpt[parent] + 1
    ac[now][0] = parent

    for i in range(1, maxPower + 1):
        ac[now][i] = ac[ac[now][i - 1]][i - 1]

    for next_node in adj[now]:
        if next_node == parent:
            continue
        dfs(next_node, now)

    ed[now] = num


def lca(x, y):
    if dpt[x] > dpt[y]:
        x, y = y, x
    for i in range(maxPower, -1, -1):
        if dpt[y] - dpt[x] >= (1 << i):
            y = ac[y][i]
    if x == y:
        return x
    for i in range(maxPower, -1, -1):
        if ac[x][i] != ac[y][i]:
            x = ac[x][i]
            y = ac[y][i]
    return ac[x][0]


def modify(n, s, e, idx, diff):
    if idx < s or idx > e:
        return
    tree[n] += diff
    if s == e:
        return
    mid = (s + e) // 2
    modify(n << 1, s, mid, idx, diff)
    modify(n << 1 | 1, mid + 1, e, idx, diff)


def query(n, s, e, l, r):
    if l > e or r < s:
        return 0
    if l <= s and e <= r:
        return tree[n]
    mid = (s + e) // 2
    return query(n << 1, s, mid, l, r) + query(n << 1 | 1, mid + 1, e, l, r)


def main():
    global N, M
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(2, N + 1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    dfs(1, 0)

    for _ in range(M):
        cmd, a, b = sys.stdin.readline().split()
        a, b = int(a), int(b)
        if cmd == 'P':
            next_node = lca(a, b)
            modify(1, 1, N, st[next_node], -2)
            modify(1, 1, N, st[a], 1)
            modify(1, 1, N, st[b], 1)
        else:
            if st[a] < st[b]:
                next_node = b
            else:
                next_node = a
            print(query(1, 1, N, st[next_node], ed[next_node]))


if __name__ == "__main__":
    main()
