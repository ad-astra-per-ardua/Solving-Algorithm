import sys
input = sys.stdin.readline

p = [[0]*101 for _ in range(101)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            p[i][j] = 1

for i in range(1, 101):
    for j in range(101):
        if p[i][j] and p[i-1][j]:
            p[i][j] = p[i-1][j] + 1

m = 0
for i in range(101):
    for j in range(101):
        h = p[i][j]
        for k in range(j, 101):
            if p[i][k] == 0:
                break
            h = min(h, p[i][k])
            m = max(m, h*(k-j+1))
print(m)
