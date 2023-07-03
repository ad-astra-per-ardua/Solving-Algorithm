import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

n, m = map(int, input().split())
p = list(range(n))

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if find(a) == find(b):
        cycle = i
        break
    union(a, b)
else:
    cycle = 0

print(cycle)
