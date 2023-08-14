import sys
input = sys.stdin.readline

log = 19

M = int(input())
dp = [[0 for _ in range(M + 1)] for _ in range(log + 1)]
line = list(map(int, input().split()))

for i in range(1, M + 1):
    dp[0][i] = line[i - 1]

for i in range(1, log + 1):
    for j in range(1, M + 1):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

Q = int(input())
results = []

for _ in range(Q):
    n, x = map(int, input().split())
    for b in range(log):
        if (n & (1 << b)) > 0:
            x = dp[b][x]
    results.append(x)

for r in results:
    print(r)
print('"C:\Download\\\'hello\'.py"')