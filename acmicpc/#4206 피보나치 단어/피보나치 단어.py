import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

def failure(B, fail):
    n = len(B)
    fail[0] = -1
    for start in range(1, n):
        before = fail[start - 1]
        while (before >= 0) and (B[before + 1] != B[start]):
            before = fail[before]
        if B[before + 1] == B[start]:
            fail[start] = before + 1
        else:
            fail[start] = -1

def kmpSearch(A, B, fail):
    count = 0
    i, j = 0, -1
    n, m = len(A), len(B)
    while i < n:
        if j < m - 1 and A[i] == B[j + 1]:
            if j + 1 == m - 1:
                j = fail[j + 1]
                count += 1
            else:
                j += 1
            i += 1
        else:
            if j == -1:
                i += 1
            else:
                j = fail[j]
    return count

def F(i, count, cached, m, p, fail):
    if i > n:
        return cached[i - 1]
    mid = m[0] if count == 0 else m[1] if count % 2 == 1 else m[2]

    isFind = 0
    if len(p) > 1:
        isFind = kmpSearch(mid, p, fail)

    cached[i] = cached[i - 1] + cached[i - 2] + isFind
    return F(i + 1, count + 1, cached, m, p, fail)

def solve(n, p):
    tmpstr = ["0", "1"]
    fail = [-1 for _ in range(len(p))]
    failure(p, fail)
    i = 0
    while len(tmpstr[0]) < len(p):
        i += 1
        tmp = tmpstr[1] + tmpstr[0]
        tmpstr[0], tmpstr[1] = tmpstr[1], tmp

    if n < i:
        return 0

    cached = [0 for _ in range(111)]
    cached[i] = kmpSearch(tmpstr[0], p, fail)
    cached[i + 1] = kmpSearch(tmpstr[1], p, fail)

    fs = len(tmpstr[1]) - len(p) + 1
    bs = len(tmpstr[0]) - len(p) + 1
    w = len(p) * 2 - 2
    m = [
        (tmpstr[1] + tmpstr[0])[fs:fs + w],
        (tmpstr[0] + tmpstr[1])[bs:bs + w],
        (tmpstr[1] + tmpstr[1])[fs:fs + w]
    ]

    result = F(i + 2, 0, cached, m, p, fail)
    return cached[i] if n == i else cached[i + 1] if n == i + 1 else result

if __name__ == "__main__":
    i = 1
    while True:
        line = input().strip()
        if not line:
            break
        n = int(line)
        p = input().strip()
        if n < 0:
            break
        print(f"Case {i}:", solve(n, p))
        i += 1
