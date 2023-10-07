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
    j, n = map(int, input().split())

    cnt = 0

    for _ in range(n):
        s = input().strip()

        val = 0

        for c in s:
            if 'A' <= c <= 'Z':
                val += 4
            elif 'a' <= c <= 'z' or '0' <= c <= '9':
                val += 2
            else:
                val += 1

        if val <= j:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
