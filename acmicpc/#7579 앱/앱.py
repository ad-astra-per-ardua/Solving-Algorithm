import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mem = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [0 for _ in range(sum(cost) + 1)]
max_cost = sum(cost)

for i in range(n):
    for j in range(max_cost, cost[i]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[i]] + mem[i])

for i in range(max_cost + 1):
    if dp[i] >= m:
        print(i)
        break
