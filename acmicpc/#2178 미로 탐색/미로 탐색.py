from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
direction_x = [1, 0, -1, 0]
direction_y = [0, 1, 0, -1]
array = []

for _ in range(n):
    array.append(list(map(int, list(input().strip()))))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1


def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        cy, cx = queue.popleft()
        for k in range(4):
            ny = cy + direction_y[k]
            nx = cx + direction_x[k]
            if 0 <= ny < n and 0 <= nx < m:
                if array[ny][nx] == 1 and visited[ny][nx] == False:
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[cy][cx] + 1
    return visited[n - 1][m - 1]


print(bfs(0, 0))
