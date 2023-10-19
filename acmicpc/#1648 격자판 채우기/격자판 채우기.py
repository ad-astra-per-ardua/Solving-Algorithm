import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 9901
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

def dpf(k, s):
    if k == n * m and s == 0:
        return 1
    if k >= n * m:
        return 0
    if dp[k][s] != -1:
        return dp[k][s]

    ret = 0
    if s & 1:
        ret = dpf(k + 1, s >> 1)
    else:
        ret += dpf(k + 1, (s >> 1) | (1 << (m - 1)))
        if (k % m) != (m - 1) and not (s & 2):
            ret += dpf(k + 2, s >> 2)
    dp[k][s] = ret % MOD
    return dp[k][s]


n, m = map(int, input().split())
dp = [[-1] * (1 << m) for _ in range(n * m)]
print(dpf(0, 0))