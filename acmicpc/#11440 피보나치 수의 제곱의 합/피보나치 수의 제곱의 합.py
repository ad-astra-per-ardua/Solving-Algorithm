mod = 10**9+7

m = [{}, {}]

def fibo(x, idx):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    elif x in m[idx]:
        return m[idx][x]

    if x % 2 == 0:
        tmp1 = fibo(x // 2 + 1, idx) % mod
        tmp2 = fibo(x // 2 - 1, idx) % mod
        tmp1 = (tmp1 * tmp1) % mod
        tmp2 = (tmp2 * tmp2) % mod
        m[idx][x] = (tmp1 - tmp2 + mod) % mod
    else:
        tmp1 = fibo(x // 2, idx) % mod
        tmp2 = fibo(x // 2 + 1, idx) % mod
        tmp1 = (tmp1 * tmp1) % mod
        tmp2 = (tmp2 * tmp2) % mod
        m[idx][x] = (tmp1 + tmp2) % mod

    return m[idx][x]

n = int(input().strip())

tmp1 = fibo(n + 1, 0)
tmp2 = fibo(n, 1)
tmp1 = tmp1 * tmp1 % mod
tmp2 = tmp2 * tmp2 % mod
result = tmp1 - tmp2 + (-1 if n%2==0 else 1)

print((result + mod) % mod)
