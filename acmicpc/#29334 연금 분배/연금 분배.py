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

mod = 1_000_000_007
# sys.setrecursionlimit(100_000_000)
input = lambda: stdstr().strip()
# main code goes here

def main():
    n = int(input())
    q = [0.0] + list(map(float, input().split()))
    r = [0.0] + list(map(float, input().split()))

    prefix_sum = [0.0] * (n + 1)

    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + r[i]

    ret = [0.0] * (n + 1)
    total = 0.0

    for i in range(1, n + 1):
        ret[i] = q[i] / (prefix_sum[n] - prefix_sum[i - 1])
        total += ret[i]

    for i in range(1, n + 1):
        print("{:.6f}".format(ret[i] / total), end=" ")
    print()

if __name__ == "__main__":
    main()
