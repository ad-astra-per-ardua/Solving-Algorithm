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
    n = int(input())
    s = input().strip()

    s_cnt = [0] * 26

    for c in s:
        s_cnt[ord(c) - ord('A')] += 1

    bs = "BRONZESILVER"

    bs_cnt = [0] * 26

    for c in bs:
        bs_cnt[ord(c) - ord('A')] += 1

    ans = 1e9

    for i in range(26):
        if bs_cnt[i] == 0:
            continue

        ans = min(ans, s_cnt[i] // bs_cnt[i])

    print(ans)


if __name__ == "__main__":
    main()
