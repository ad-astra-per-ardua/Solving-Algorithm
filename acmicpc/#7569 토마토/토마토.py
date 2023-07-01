from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        a, b, c = q.popleft()
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < h and 0 <= y < n and 0 <= z < m and s[x][y][z] == 0:
                q.append([x, y, z])
                s[x][y][z] = s[a][b][c] + 1

m, n, h = map(int, input().split())
s = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if s[i][j][k] == 1:
                q.append([i, j, k])
bfs()

flag = 1
result = -2

for i in s:
    for j in i:
        for k in j:
            if k == 0:
                flag = 0
            result = max(result, k)

if flag == 0:
    print(-1)
else:
    print(result - 1)
