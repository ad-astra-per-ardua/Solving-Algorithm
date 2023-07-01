import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()
str3 = input().strip()

dp = [[[0] * (len(str3) + 1) for _ in range(len(str2) + 1)] for __ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        for k in range(1, len(str3) + 1):
            if str1[i-1] == str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])
