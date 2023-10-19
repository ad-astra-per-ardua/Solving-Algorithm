import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

from collections import deque

class MCMF:
    def __init__(self, n=0, s=-1, t=-1):
        self.n = n
        self.c = [[0]*1010 for _ in range(1010)]
        self.f = [[0]*1010 for _ in range(1010)]
        self.d = [[0]*1010 for _ in range(1010)]
        self.g = [[] for _ in range(1010)]
        self.source = s
        self.sink = t

    def setSource(self, s):
        self.source = s

    def setSink(self, t):
        self.sink = t

    def addEdge(self, s, e, cap, dist):
        self.g[s].append(e)
        self.c[s][e] = cap
        self.d[s][e] = dist

        self.g[e].append(s)
        self.c[e][s] = 0
        self.d[e][s] = -dist

    def mcmf(self):
        cnt = 0
        minCost = 0
        prv = [-1]*1010
        dist = [float('inf')]*1010
        inque = [0]*1010

        while True:
            prv = [-1]*1010
            dist = [float('inf')]*1010
            inque = [0]*1010
            q = deque()
            dist[self.source] = 0
            inque[self.source] = 1
            q.append(self.source)

            while q:
                now = q.popleft()
                inque[now] = 0
                for nxt in self.g[now]:
                    if self.c[now][nxt] - self.f[now][nxt] > 0 and dist[nxt] > dist[now] + self.d[now][nxt]:
                        dist[nxt] = dist[now] + self.d[now][nxt]
                        prv[nxt] = now
                        if not inque[nxt]:
                            q.append(nxt)
                            inque[nxt] = 1

            if prv[self.sink] == -1:
                break

            flow = float('inf')
            i = self.sink
            while i != self.source:
                flow = min(flow, self.c[prv[i]][i] - self.f[prv[i]][i])
                i = prv[i]

            i = self.sink
            while i != self.source:
                minCost += flow * self.d[prv[i]][i]
                self.f[prv[i]][i] += flow
                self.f[i][prv[i]] -= flow
                i = prv[i]

            cnt += 1

        return cnt, minCost

if __name__ == '__main__':
    n, m = map(int, input().split())
    flow = MCMF(1002, 1001, 1002)

    for i in range(1, n+1):
        flow.addEdge(1001, i, 1, 0)

    for i in range(501, 501+m):
        flow.addEdge(i, 1002, 1, 0)

    for i in range(1, n+1):
        data = list(map(int, input().split()))
        cnt = data[0]
        for j in range(cnt):
            a, b = data[j*2+1], data[j*2+2]
            flow.addEdge(i, 500+a, 1, b)

    tasks, cost = flow.mcmf()
    print(tasks)
    print(cost)
