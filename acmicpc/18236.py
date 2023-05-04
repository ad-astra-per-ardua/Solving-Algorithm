import sys

n = int(sys.stdin.readline().rstrip())
matrix_sizes = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    matrix_sizes.append((r, c))

dp = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

for k in range(1, n):
    for i in range(n - k):
        j = i + k
        for m in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j] + matrix_sizes[i][0] * matrix_sizes[m][1] * matrix_sizes[j][1])

print(dp[0][n-1])