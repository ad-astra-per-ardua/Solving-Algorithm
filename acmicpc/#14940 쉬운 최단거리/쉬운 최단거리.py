from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
distance = [[-1 for _ in range(m)] for _ in range(n)]
start = deque()

for i in range(n):
    k = list(map(int, input().split()))
    for j in range(len(k)):
        if k[j] == 2:
            start = (i, j)
    graph.append(k)

direction_x = [1, 0, -1, 0]
direction_y = [0, 1, 0, -1]


def bfs(graph, start):
    queue = deque([start])
    visited[start[0]][start[1]] = 1
    distance[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + direction_x[i], y + direction_y[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append([nx, ny])
                elif graph[nx][ny] == 0:
                    distance[nx][ny] = 0

bfs(graph, start)

for i in range(n):
    for j in range(m):
        if distance[i][j] == -1 and graph[i][j] == 0:
            distance[i][j] = 0

for e in distance:
    print(*e)