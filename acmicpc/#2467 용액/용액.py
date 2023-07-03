import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

l = 0
r = n - 1
s = a[l] + a[r]
p = (a[l], a[r])

while l < r:
    t = a[l] + a[r]
    if abs(t) < abs(s):
        s = t
        p = (a[l], a[r])

    if t < 0:
        l += 1
    else:
        r -= 1

print(*sorted(p))
