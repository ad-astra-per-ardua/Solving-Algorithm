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

MAX = 100000
a = [0] * (MAX + 1)
tree = [[] for _ in range(MAX * 4 + 1)]

def init(start, end, node, index, x):
    if start > index or index > end: return
    tree[node].append(x)
    if start == end: return
    mid = (start + end) // 2
    init(start, mid, node * 2, index, x)
    init(mid + 1, end, node * 2 + 1, index, x)

def query(start, end, node, left, right, k):
    if start > right or end < left: return 0
    if left <= start and end <= right:
        return len(tree[node]) - bisect_right(tree[node], k)
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right, k) + query(mid + 1, end, node * 2 + 1, left, right, k)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    for i, val in enumerate(arr, 1):
        a[i] = val
        init(1, n, 1, i, a[i])

    for t in tree:
        t.sort()

    last_ans = 0
    m = int(input())
    for _ in range(m):
        left, right, k = map(int, input().split())
        left ^= last_ans
        right ^= last_ans
        k ^= last_ans
        last_ans = query(1, n, 1, left, right, k)
        print(last_ans)

if __name__ == "__main__":
    main()