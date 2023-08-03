import sys
from collections import Counter

input = sys.stdin.readline

def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def dir(a, b, c):
    dxab = b.x - a.x
    dxac = c.x - a.x
    dyab = b.y - a.y
    dyac = c.y - a.y

    if dxab * dyac < dyab * dxac: dir = 1
    elif dxab * dyac > dyab * dxac: dir = -1
    else:
        if dxab == 0 and dyab == 0: dir = 0
        if dxab * dxac < 0 or dyab * dyac < 0: dir = -1
        elif dxab * dxab + dyab * dyab >= dxac * dxac + dyac * dyac: dir = 0
        else: dir = 1
    return dir

def intersec(l1, l2):
    if dir(l1.p1, l1.p2, l2.p1) * dir(l1.p1, l1.p2, l2.p2) <= 0 and \
        dir(l2.p1, l2.p2, l1.p1) * dir(l2.p1, l2.p2, l1.p2) <= 0:
        return True
    return False

N = int(input())
lines = []
p = [i for i in range(N)]

for i in range(N):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    line = Line(Point(x1, y1), Point(x2, y2))
    lines.append(line)

for i in range(N):
    for j in range(i+1, N):
        if intersec(lines[i], lines[j]):
            union_parent(p, i, j)

p = [find_parent(p, x) for x in p]
cnt = Counter(p)
print(len(cnt))
print(max(cnt.values())) 
