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
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def main():
    dx = [-2, 2, 0, 0]
    dy = [0, 0, -2, 2]

    n, k = map(int, input().split())

    points = [Point() for _ in range(k)]
    st = set()

    for i in range(k):
        x, y = map(int, input().split())
        points[i].x = x
        points[i].y = y
        st.add((x - 1) * 100000 + y - 1)

    ans_st = set()

    for i in range(k):
        x = points[i].x
        y = points[i].y

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx <= 0 or nx > n or ny <= 0 or ny > n:
                continue

            val = (nx - 1) * 100000 + ny - 1

            if val not in st:
                ans_st.add(val)

    print(len(ans_st))


if __name__ == "__main__":
    main()
