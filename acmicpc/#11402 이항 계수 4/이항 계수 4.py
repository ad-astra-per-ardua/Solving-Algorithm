import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)


def b_mial(n, k, p):
    if temp1[n][k] != 0:
        return temp1[n][k]

    if k == 0 or n == k:
        temp1[n][k] = 1
        return temp1[n][k]

    temp1[n][k] = (b_mial(n-1, k-1, p) + b_mial(n-1, k, p) % p)
    return temp1[n][k]


def digit(n, b):
    d = []
    while n:
        d.append(n % b)
        n //= b
    return d


def lucas(n, k, p):
    temp = 1
    cf = digit(n, p)
    boj = digit(k, p)

    for i in range(max(len(cf), len(boj))):
        tp1, tp2 = 0, 0
        if i < len(cf):
            tp1 = cf[i]
        else:
            tp1 = 0
        if i < len(boj):
            tp2 = boj[i]
        else:
            tp2 = 0
        if tp1 < tp2:
            return 0
        temp = (temp * b_mial(tp1, tp2, p) % p)
    return temp


n, k, m = map(int, input().split())
temp1 = [[0 for _ in range(2001)] for _ in range(2001)]

print(lucas(n, k, m))