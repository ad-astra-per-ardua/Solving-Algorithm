# Origin source from Ana_naS

import sys
input = sys.stdin.readline

dp = [0] * 2000000
dp[1] = 1
dp[2] = 5
dp[3] = 10
j = 4
for i in range(3, 1600):
    dp[j] = dp[j - i + 1] + j * j
    for j in range(j + 1, j + i - 1):
        dp[j] = dp[j - i] + dp[j - i + 1] - dp[j - 2 * i + 2] + j * j
    j += 1
    dp[j] = dp[j - i] + j * j
    j += 1

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
