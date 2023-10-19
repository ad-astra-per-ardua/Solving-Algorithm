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
def main():
    n = int(input())
    a, b, c = map(int, input().split())
    v = [0] + list(map(int, input().split()))
    s = [0] * (n + 1)
    dp = [0] * (n + 1)
    xpos = [-1e9] * (n + 1)
    stk = [0] * (n + 1)
    scnt = 0
    pt = 1

    for i in range(1, n + 1):
        s[i] = s[i - 1] + v[i]

    def func(x):
        return a * x * x + b * x + c

    def k(i):
        return -2 * a * s[i]

    def m(i):
        return a * s[i] * s[i] - b * s[i] + dp[i]

    def getCross(p, q):
        k1 = k(p)
        m1 = m(p)
        k2 = k(q)
        m2 = m(q)
        return (m1 - m2) / (k2 - k1)

    for i in range(1, n + 1):
        dp[i] = func(s[i])
        if scnt:
            while pt < scnt and xpos[pt + 1] < s[i]:
                pt += 1
            j = stk[pt]
            dp[i] = max(dp[i], dp[j] + func(s[i] - s[j]))

            while scnt > 1 and xpos[scnt] > getCross(stk[scnt], i):
                scnt -= 1
            scnt += 1
            stk[scnt] = i
            xpos[scnt] = getCross(stk[scnt - 1], i)
            if pt > scnt:
                pt = scnt
        else:
            scnt += 1
            stk[scnt] = i
            xpos[scnt] = -1e9

    print(dp[n])

main()
