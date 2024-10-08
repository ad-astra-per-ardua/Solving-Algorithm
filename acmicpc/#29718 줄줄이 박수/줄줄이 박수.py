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

def main():
    n, m = map(int, input().split())

    vec = [0] * (m + 1)

    for _ in range(n):
        row_values = list(map(int, input().split()))
        for col, x in enumerate(row_values):
            vec[col + 1] += x

    for col in range(1, m + 1):
        vec[col] += vec[col - 1]

    a = int(input())

    ans = 0

    for col in range(a, m + 1):
        ans = max(ans, vec[col] - vec[col - a])

    print(ans)


if __name__ == "__main__":
    main()
