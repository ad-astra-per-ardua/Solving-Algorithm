import sys

input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
#   기본 자료구조 세팅

direction_y = [0, 1, 0, -1]
direction_x = [1, 0, -1, 0]


def bfs(y, x):
    result = 1
    queue = [(y, x)]
    while queue:
        now_y, now_x = queue.pop()
        for k in range(4):
            next_y = now_y + direction_y[k]
            next_x = now_x + direction_x[k]
            if 0 <= next_y < n and 0 <= next_x < m:
                if array[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                    result += 1
                    visited[next_y][next_x] = True
                    queue.append((next_y, next_x))
    return result


count = 0
max_v = 0
for j in range(n):
    for i in range(m):
        if array[j][i] == 1 and visited[j][i] == False:
            visited[j][i] = True
            count += 1
            max_v = max(max_v, bfs(j, i))
print(count)
print(max_v)
