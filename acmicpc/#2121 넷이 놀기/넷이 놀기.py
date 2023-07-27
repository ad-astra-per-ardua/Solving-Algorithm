import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int, input().split())
coords = {}
for _ in range(N):
    a, b = map(int, input().split())
    if (a, b) in coords:
        coords[(a, b)] += 1
    else:
        coords[(a, b)] = 1


res = 0
for key in coords:
    x, y = key
    if (x + A, y + B) in coords and (x + A, y) in coords and (x, y + B) in coords:
        res += min(coords[(x, y)], coords[(x + A, y + B)], coords[(x, y + B)], coords[(x + A, y)])

print(res)
