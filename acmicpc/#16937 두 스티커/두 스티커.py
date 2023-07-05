import sys

input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]
max_a = 0

for i in range(n):
    for j in range(i + 1, n):
        for a in [s[i], s[i][::-1]]:
            for b in [s[j], s[j][::-1]]:
                if a[0] + b[0] <= h and max(a[1], b[1]) <= w:
                    max_a = max(max_a, a[0] * a[1] + b[0] * b[1])
                if max(a[0], b[0]) <= h and a[1] + b[1] <= w:
                    max_a = max(max_a, a[0] * a[1] + b[0] * b[1])

print(max_a)
