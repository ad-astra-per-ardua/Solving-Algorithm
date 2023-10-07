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

n, m = map(int, input().split())
x, y = map(int, input().split())

m0, m1 = 0, 0

for _ in range(m):
    a, b = map(int, input().split())
    if a == 0:
        m0 += 1
    else:
        m1 += 1

cnt = 1
ii = n - m1
ie = m0

for i in range(ie):
    cnt *= ii
    ii -= 1

ii = 9 - m
ie = n - m

for i in range(ie):
    cnt *= ii
    ii -= 1

ans = cnt * x + (cnt - 1) // 3 * y
print(ans)
