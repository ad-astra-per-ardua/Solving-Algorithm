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

MOD = 1_000_000_007
# sys.setrecursionlimit(100_000_000)
input = lambda: stdstr().strip()
############## main code goes here ##############

def solve():
    T = int(input())
    for _ in range(T):
        m, n = map(int, input().split())
        g = [list(map(int, input().split())) for _ in range(m)]
        d = 0
        for j in range(n):
            f = 0
            dm = 0
            for i in range(m - 1, -1, -1):
                if g[i][j] == 1:
                    dm += f
                else:
                    f += 1

            d += dm
        print(d)

if __name__ == "__main__":
    solve()
