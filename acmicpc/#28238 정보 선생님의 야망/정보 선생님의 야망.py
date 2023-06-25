import sys

input = sys.stdin.readline

loop = int(input())
d = [0] * 10
for _ in range(loop):
    *l, = map(int, input().split())
    k = 0
    for j in range(5):
        for i in range(j):
            d[k] += l[i] & l[j]
            k += 1
x = 0
y = 1
z = d[0]
k = 0
for j in range(5):
    for i in range(j):
        if d[k] > +z:
            x = i
            y = j
            z = d[k]
        k += 1
print(z)
l = [0] * 5
l[x] = l[y] = 1
print(*l)
