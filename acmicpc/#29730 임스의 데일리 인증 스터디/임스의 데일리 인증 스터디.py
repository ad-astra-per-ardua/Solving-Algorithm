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
import re

def cmp_str(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    return (a > b) - (a < b)


def main():
    n = int(input())

    vec = []
    boj_vec = []

    p = re.compile(r'boj\.kr/([0-9]+)')

    for _ in range(n):
        s = input()

        m = p.match(s)
        if m:
            boj_vec.append(int(m.group(1)))
        else:
            vec.append(s)

    vec.sort(key=lambda x: (len(x), x))
    boj_vec.sort()

    for s in vec:
        print(s)

    for i in boj_vec:
        print(f"boj.kr/{i}")


if __name__ == "__main__":
    main()
