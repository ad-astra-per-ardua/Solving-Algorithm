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
input = lambda: stdstr().strip()
# main code goes here
MOD = 1000000007

def factorial():
    fact[0] = 1
    fact[1] = 1
    for i in range(2, 2000001):
        fact[i] = fact[i - 1] * i % MOD

def factorial_inverse():
    inv_fact[0] = 1
    inv_fact[1] = 1
    for i in range(2, 2000001):
        inv_fact[i] = inv_fact[MOD % i] * (MOD - MOD // i) % MOD

def factorial_inverse_2():
    inv_fact2[0] = 1
    inv_fact2[1] = 1
    for i in range(2, 2000001):
        inv_fact2[i] = inv_fact2[i - 1] * inv_fact[i] % MOD

def backtracking(curr):
    global res
    kk = 1
    last = len(check)
    check.append((n, m))
    for i in range(last):
        dx = check[i + 1][0] - check[i][0]
        dy = check[i + 1][1] - check[i][1]
        kk *= fact[dx + dy]
        kk %= MOD
        kk *= inv_fact2[dy]
        kk %= MOD
        kk *= inv_fact2[dx]
        kk %= MOD
    check.pop()
    if last % 2 == 0:
        res = (res + MOD - kk) % MOD
    else:
        res += kk

    for i in range(curr + 1, k):
        if bombs[curr][1] > bombs[i][1]:
            continue
        check.append(bombs[i])
        backtracking(i)
        check.pop()

def solve():
    global n, m, k, res, bombs
    n, m, k = map(int, input().split())
    factorial()
    factorial_inverse()
    factorial_inverse_2()
    res *= fact[n + m]
    res %= MOD
    res *= inv_fact2[m]
    res %= MOD
    res *= inv_fact2[n]
    res %= MOD
    for _ in range(k):
        x, y = map(int, input().split())
        bombs.append((x, y))

    bombs.sort()

    for i in range(k):
        check.append(bombs[i])
        backtracking(i)
        check.pop()

    print(res)

if __name__ == "__main__":
    fact = [0] * 2000001
    inv_fact = [0] * 2000001
    inv_fact2 = [0] * 2000001
    res = 1
    check = [(0, 0)]
    bombs = []
    solve()
