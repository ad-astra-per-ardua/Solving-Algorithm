s = input()
n = len(s)
MOD = 10007

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    dp[i][i+1] = 2 + (s[i] == s[i+1])

for l in range(3, n+1):
    for i in range(n-l+1):
        j = i + l - 1
        if s[i] == s[j]:
            dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % MOD
        else:
            dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD

print(dp[0][n-1])
