import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, visited, graph):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

n = int(input())
normal = [list(input().strip()) for _ in range(n)]
blind = [[y if y != 'G' else 'R' for y in x] for x in normal]

normal_visited = [[0]*n for _ in range(n)]
blind_visited = [[0]*n for _ in range(n)]

normal_res = 0
blind_res = 0

for i in range(n):
    for j in range(n):
        if normal_visited[i][j] == 0:
            bfs((i, j), normal_visited, normal)
            normal_res += 1
        if blind_visited[i][j] == 0:
            bfs((i, j), blind_visited, blind)
            blind_res += 1

print(normal_res, blind_res)
