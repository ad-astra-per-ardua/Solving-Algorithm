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

def FFT(v, inv):
    S = len(v)

    i, j = 1, 0
    while i < S:
        bit = S // 2
        while j >= bit:
            j -= bit
            bit //= 2
        j += bit

        if i < j:
            v[i], v[j] = v[j], v[i]

        i += 1

    k = 1
    while k < S:
        angle = cmath.pi / k if inv else -cmath.pi / k
        w = complex(cmath.cos(angle), cmath.sin(angle))

        i = 0
        while i < S:
            z = complex(1, 0)
            for j in range(k):
                even = v[i + j]
                odd = v[i + j + k]

                v[i + j] = even + z * odd
                v[i + j + k] = even - z * odd
                z *= w
            i += 2 * k

        k *= 2

    if inv:
        for i in range(S):
            v[i] /= S

    return v

def mul(v, u):
    S = 2
    while S < len(v) + len(u):
        S *= 2

    v += [complex(0, 0)] * (S - len(v))
    u += [complex(0, 0)] * (S - len(u))

    v = FFT(v, False)
    u = FFT(u, False)

    w = [v[i] * u[i] for i in range(S)]
    w = FFT(w, True)

    return w

def main():
    v = [complex(0, 0)] * 60001
    u = [complex(0, 0)] * 60001
    w = [complex(0, 0)] * 60001

    N = int(input())
    for x in map(int, input().split()):
        v[x + 30000] = complex(1, 0)

    M = int(input())
    for x in map(int, input().split()):
        u[x + 30000] = complex(1, 0)

    K = int(input())
    for x in map(int, input().split()):
        w[x + 30000] = complex(1, 0)

    vw = mul(v, w)

    ans = 0
    for i in range(60001):
        ans += round(u[i].real) * round(vw[i * 2].real)

    print(ans)

if __name__ == '__main__':
    main()
