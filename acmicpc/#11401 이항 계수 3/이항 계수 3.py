import sys
input = sys.stdin.readline

N, K = map(int, input().split())
mod = 1000000007

def ftr(N):
    n = 1
    for i in range(2, N + 1):
        n = (n * i) % mod
    return n


def sqr(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    temp = sqr(n, k // 2)
    if k % 2:
        return temp * temp * n % mod
    else:
        return temp * temp % mod


top = ftr(N)
bot = ftr(N - K) * ftr(K) % mod


print(top * sqr(bot, mod- 2) % mod)