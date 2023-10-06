import sys
import math
import bisect
import time
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, lcm
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
def flush(): return stdout.flush()
def stdstr(): return stdin.readline()

mod = 10_0000_0007
# sys.setrecursionlimit(1_0000_0000)
input = lambda: sys.stdin.readline().strip()
# main code goes here

MAXN = 28

str_ = [['.' * MAXN for _ in range(MAXN)] for _ in range(2)]
dp = [[[[[-1 for _ in range(MAXN)] for _ in range(MAXN)] for _ in range(MAXN)] for _ in range(MAXN)] for _ in range(2)]

def f(p, sx, ex, sy, ey):
    if sx > ex or sy > ey:
        return 0
    if dp[p][sx][ex][sy][ey] != -1:
        return dp[p][sx][ex][sy][ey]
    
    s = set()
    for i in range(sx, ex + 1):
        for j in range(sy, ey + 1):
            if str_[p][i][j] == '.':
                continue
            if str_[p][i][j] == 'R':
                l = f(p, sx, i - 1, sy, ey)
                r = f(p, i + 1, ex, sy, ey)
                s.add(l ^ r)
            elif str_[p][i][j] == 'B':
                l = f(p, sx, ex, sy, j - 1)
                r = f(p, sx, ex, j + 1, ey)
                s.add(l ^ r)
            elif str_[p][i][j] == 'G':
                a = f(p, sx, i - 1, sy, j - 1)
                b = f(p, sx, i - 1, j + 1, ey)
                c = f(p, i + 1, ex, sy, j - 1)
                d = f(p, i + 1, ex, j + 1, ey)
                s.add(a ^ b ^ c ^ d)
    
    g = 0
    while g in s:
        g += 1
    
    dp[p][sx][ex][sy][ey] = g
    return g

def main():
    n, m = map(int, input().split())
    for i in range(n):
        s = input().strip()
        for j in range(m):
            str_[(i + j) % 2][(i + j) // 2] = list(str_[(i + j) % 2][(i + j) // 2]) 
            str_[(i + j) % 2][(i + j) // 2][(i - j + m - 1) // 2] = s[j]

    ans = f(0, 0, 25, 0, 25) ^ f(1, 0, 25, 0, 25)
    if ans:
        print("W")
    else:
        print("L")

if __name__ == "__main__":
    main()