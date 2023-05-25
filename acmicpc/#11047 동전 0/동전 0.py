import sys
input = sys.stdin.readline
n, k = map(int,input().split())
change = []
coins = 0
for _ in range(n):
    change.append(int(input()))
for i in range(n):
    if k >= change[n-1-i]:
        coins += k // change[n - 1 - i]
        k %= change[n-1-i]
        if k == 0:
            break
print(coins)

