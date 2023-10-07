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
############## main code goes here ##############

def find(parent, node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find(parent, parent[node])
        return parent[node]


def process_union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return

    parent[a] = b


def main():
    n = int(input())
    parent = [0] * (n + 1)
    nums = [0] * (n + 1)
    nums_inv = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i

    num_list = list(map(int, input().split()))
    for i in range(1, n + 1):
        num = num_list[i - 1]
        nums[i] = num
        nums_inv[num] = i
        process_union(parent, i, num)

    ret = -1

    for i in range(1, n + 1):
        if find(parent, i) == i:
            ret += 1

    print(f"{ret} {ret}")

    for i in range(1, n):
        if find(parent, i) != find(parent, i + 1):
            print(f"{nums_inv[i]} {nums_inv[i + 1]}")

            nums_inv[i], nums_inv[i + 1] = nums_inv[i + 1], nums_inv[i]
            process_union(parent, i, i + 1)


if __name__ == "__main__":
    main()
