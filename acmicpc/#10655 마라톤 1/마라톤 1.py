import sys
input = sys.stdin.readline

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

total = 0
for i in range(1, n):
    total += abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])

skip = 0
for i in range(1, n - 1):
    before = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])
    after = abs(x[i + 1] - x[i]) + abs(y[i + 1] - y[i])
    direct = abs(x[i + 1] - x[i - 1]) + abs(y[i + 1] - y[i - 1])
    skip = max(skip, before + after - direct)

print(total - skip)
