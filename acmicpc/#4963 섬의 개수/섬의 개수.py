import sys
input = sys.stdin.readline

direction_x = [1, 0, -1, 0, 1, 1, -1, -1]
direction_y = [0, 1, 0, -1, 1, -1, 1, -1]
# setting data structures

def bfs(x, y):
    queue = [(x, y)]
    while queue:
        now_x, now_y = queue.pop()
        for k in range(8):
            nx = now_x + direction_x[k]
            ny = now_y + direction_y[k]
            if 0 <= nx < w and 0 <= ny < h:
                if array[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    queue.append((nx, ny))
    return


while True:
    w, h = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    if w == 0 and h == 0:
        break
    for i in range(h):
        for j in range(w):
            if array[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                count += 1
                bfs(j, i)
    print(count)


