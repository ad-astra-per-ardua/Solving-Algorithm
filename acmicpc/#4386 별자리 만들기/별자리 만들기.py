import sys
import heapq
import math

input = sys.stdin.readline

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        p[y] = x

n = int(input())
p = [i for i in range(n)]
q = []
s = []

for i in range(n):
    x, y = map(float, input().split())
    s.append([x, y])

for i in range(n):
    for j in range(i+1, n):
        heapq.heappush(q, [math.sqrt((s[i][0]-s[j][0])**2 + (s[i][1]-s[j][1])**2), i, j])

res = 0
while q:
    c, a, b = heapq.heappop(q)
    if find(a) != find(b):
        union(a, b)
        res += c

print(round(res, 2))
