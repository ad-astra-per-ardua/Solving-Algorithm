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

def f(a, b):
    while b:
        a, b = b, a % b
    return a

class LazySeg:
    def __init__(self):
        self.tree = [0] * 404040
        self.lazy = [0] * 404040

    def pro(self, node, s, e):
        if not self.lazy[node]:
            return
        self.tree[node] += (e-s+1) * self.lazy[node]
        if s != e:
            self.lazy[node*2] += self.lazy[node]
            self.lazy[node*2+1] += self.lazy[node]
        self.lazy[node] = 0

    def update(self, node, s, e, l, r, v):
        self.pro(node, s, e)
        if r < s or e < l:
            return
        if l <= s and e <= r:
            self.tree[node] += (e-s+1) * v
            if s != e:
                self.lazy[node*2] += v
                self.lazy[node*2+1] += v
            return
        m = (s + e) // 2
        self.update(node*2, s, m, l, r, v)
        self.update(node*2+1, m+1, e, l, r, v)
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def query(self, node, s, e, x):
        self.pro(node, s, e)
        if x < s or e < x:
            return 0
        if s == e:
            return self.tree[node]
        m = (s + e) // 2
        return self.query(node*2, s, m, x) + self.query(node*2+1, m+1, e, x)

class Seg:
    def __init__(self):
        self.tree = [0] * 404040
        self.bias = 1
        while self.bias < 101010:
            self.bias <<= 1

    def update(self, x, v):
        x += self.bias
        self.tree[x] = v
        while x > 1:
            x //= 2
            self.tree[x] = f(self.tree[x * 2], self.tree[x * 2 + 1])

    def query(self, l, r):
        l += self.bias
        r += self.bias
        ret = 0
        while l < r:
            if l & 1:
                ret = f(ret, self.tree[l])
                l += 1
            if not (r & 1):
                ret = f(ret, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        if l == r:
            ret = f(ret, self.tree[r])
        return ret

n = int(input())
nums = list(map(int, input().split()))
bit = LazySeg()
seg = Seg()

for i in range(1, n+1):
    bit.update(1, 1, 100000, i, i, nums[i-1])

for i in range(1, n):
    now = bit.query(1, 1, 100000, i) - bit.query(1, 1, 100000, i+1)
    seg.update(i, abs(now))

m = int(input())
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        now = seg.query(a, b-1)
        now = f(now, bit.query(1, 1, 100000, a))
        print(now)
    else:
        bit.update(1, 1, 100000, a, b, op)
        now = bit.query(1, 1, 100000, a-1) - bit.query(1, 1, 100000, a)
        seg.update(a-1, abs(now))
        now = bit.query(1, 1, 100000, b) - bit.query(1, 1, 100000, b+1)
        seg.update(b, abs(now))
