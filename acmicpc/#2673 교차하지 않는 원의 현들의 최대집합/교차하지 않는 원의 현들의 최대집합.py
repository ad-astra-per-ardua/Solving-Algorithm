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

n = int(input())
cost = [[0]*101 for _ in range(101)]
dp = [[0]*101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    cost[a][b] = cost[b][a] = 1

for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i):
            dp[j][i] = max(dp[j][i], dp[j][k] + dp[k][i] + cost[i][j])

print(dp[1][100])
