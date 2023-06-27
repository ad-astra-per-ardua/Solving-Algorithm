import sys
input = sys.stdin.readline

mod = 1000000007

ftr = [1] * 4000001
for e in range(2, 4000001):
    ftr[e] = (ftr[e-1] * e) % mod

def inv(n):
    return sqr(ftr[n], 1000000005)

def sqr(n, k):
    if k == 1:
        return n
    temp = sqr(n, k // 2)
    if k % 2 == 0:
        return temp ** 2 % mod
    else:
        return (temp ** 2 * n) % mod

loop = int(input())
for _ in range(loop):
    N, K = map(int, input().split())
    print(ftr[N] * inv(N-K) * inv(K) % mod )