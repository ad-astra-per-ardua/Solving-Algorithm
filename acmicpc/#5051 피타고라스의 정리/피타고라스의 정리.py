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

import cmath

def fft(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    len_ = 2
    while len_ <= n:
        ang = 2 * cmath.pi / len_ * (-1 if invert else 1)
        wlen = cmath.exp(complex(0, ang))
        i = 0
        while i < n:
            w = 1
            for j in range(len_ // 2):
                u = a[i+j]
                v = a[i+j+len_//2] * w
                a[i+j] = u + v
                a[i+j+len_//2] = u - v
                w *= wlen
            i += len_
        len_ <<= 1
    if invert:
        for i in range(n):
            a[i] /= n

def multiply(a, res):
    fa = a[:]
    fft(fa, False)
    for i in range(SZ):
        fa[i] *= fa[i]
    fft(fa, True)
    for i in range(SZ):
        res[i % n] += int(fa[i].real + 0.5)

n = int(input())
SZ = 1 << 20
a = [0] * SZ
res = [0] * SZ
b = [0] * SZ
c = [0] * SZ

for i in range(1, n//2 + 1):
    if i != n - i:
        a[i * i % n] += 2
        c[2 * i * i % n] += 2
    else:
        a[i * i % n] += 1
        c[2 * i * i % n] += 1
    b[i] = i * i % n

multiply(a, res)
ans = 0
mu = 0
for i in range(1, n//2 + 1):
    if i != n - i:
        ans += res[b[i]] * 2
    else:
        ans += res[b[i]]

for i in range(1, n//2 + 1):
    if i != n - i:
        mu += c[b[i]] * 2
    else:
        mu += c[b[i]]

ans = (ans - mu) // 2 + mu
print(ans)
