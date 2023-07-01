import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
a = list(map(int,input().split()))

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp)+1)