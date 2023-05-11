a = int(input())
b = int(input())
dp = [[0]*101 for _ in range(101)]
dp[0][0] = 0

for i in range(1, a+1):
    for j in range(i*2, min(b+1, i*4+1)):
        if j-4 >= 0 and dp[i-1][j-4] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-4] + 1)
        if dp[i-1][j-2] != -1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-2])

for i in range(b, -1, -1):
    if dp[a][i] != -1:
        print(dp[a][i], a-dp[a][i])
        break
