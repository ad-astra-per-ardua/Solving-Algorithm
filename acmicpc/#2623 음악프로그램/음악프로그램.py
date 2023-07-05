import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

indeg = [0]*(n+1)
g = [[] for _ in range(n+1)]
q = deque()

for _ in range(m):
    o = list(map(int, input().split()))
    for i in range(1, len(o)):
        if i == len(o) - 1:
            break
        g[o[i]].append(o[i+1])
        indeg[o[i+1]] += 1

for i in range(1, n+1):
    if indeg[i] == 0:
        q.append(i)

result = []

while q:
    x = q.popleft()
    result.append(x)
    for i in g[x]:
        indeg[i] -= 1
        if indeg[i] == 0:
            q.append(i)

if len(result) == n:
    for i in result:
        print(i)
else:
    print(0)
