import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

v = float('inf')
r = []

for x in range(n - 2):
    y, z = x + 1, n - 1
    while y < z:
        s = a[x] + a[y] + a[z]
        if abs(s) < v:
            v = abs(s)
            r = [a[x], a[y], a[z]]

        if s < 0:
            y += 1
        else:
            z -= 1

print(*r)
