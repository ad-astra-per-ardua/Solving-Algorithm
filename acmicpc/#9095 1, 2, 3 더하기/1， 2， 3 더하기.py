import sys
input = sys.stdin.readline

loop = int(input())
test_case = []

for _ in range(loop):
    test_case.append(int(input()))

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for tc in test_case:
    print(dp[tc])
