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

def buildSA(s):
    N = len(s)
    sa = list(range(N))
    r = [0] * (2 * N)
    nr = [0] * (2 * N)

    for i in range(N):
        r[i] = ord(s[i])

    d = 1
    while d < N:
        sa.sort(key=lambda x: (r[x], r[x + d]))

        nr[sa[0]] = 1
        for i in range(1, N):
            nr[sa[i]] = nr[sa[i - 1]] + (r[sa[i - 1]] < r[sa[i]] or (r[sa[i - 1]] == r[sa[i]] and r[sa[i - 1] + d] < r[sa[i] + d]))

        r = nr[:]
        d <<= 1

    return sa

def buildLCP(s):
    N = len(s)
    sa = buildSA(s)
    lcp = [0] * N
    isa = [0] * N

    for i in range(N):
        isa[sa[i]] = i

    k = 0
    for i in range(N):
        if isa[i]:
            j = sa[isa[i] - 1]
            while i + k < N and j + k < N and s[i + k] == s[j + k]:
                k += 1
            lcp[isa[i]] = k
            if k:
                k -= 1

    return lcp

if __name__ == "__main__":
    s = input().strip()
    lcp = buildLCP(s)
    N = len(s)
    ans = N * (N + 1) // 2 - sum(lcp)
    print(ans)
