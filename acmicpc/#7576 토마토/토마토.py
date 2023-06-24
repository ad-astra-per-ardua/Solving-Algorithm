from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
array = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
direction_x = [1,0,-1,0]
direction_y = [0,1,0,-1]
day = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = direction_x[i] + x, direction_y[i] + y
            if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0:
                array[nx][ny] = array[x][y] + 1
                queue.append([nx,ny])


bfs()
for i in array:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
    day = max(day, max(i))
print(day - 1)