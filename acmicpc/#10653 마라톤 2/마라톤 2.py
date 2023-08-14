import sys
input = sys.stdin.readline
n, k = map(int, input().split())
v = [(0, 0) for _ in range(1001)]

a = [[0 for _ in range(501)] for _ in range(501)]
d = [[-1 for _ in range(501)] for _ in range(501)]

def dp(n, k):
    ret = d[n][k]
    if ret != -1:
        return ret
    if n == 1:
        return 0

    ret = float('inf')
    
    for i in range(k + 1):
        if 1 <= n - i - 1:
            ret = min(ret, dp(n - i - 1, k - i) + a[n - i - 1][n])
    
    d[n][k] = ret
    return ret

for i in range(1, n + 1):
    x, y = map(int, input().split())
    v[i] = (x, y)

for i in range(1, n):
    for j in range(i + 1, n + 1):
        a[i][j] = abs(v[i][0] - v[j][0]) + abs(v[i][1] - v[j][1])

print(dp(n, k))
