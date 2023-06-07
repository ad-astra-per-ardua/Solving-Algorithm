import sys

input = sys.stdin.readline
#  add direction with 4 direct + diagonally
direction_x = [1, 0, -1, 0, 1, 1, -1, -1]
direction_y = [0, 1, 0, -1, 1, -1, 1, -1]


def bfs(x, y):
    queue = [(x, y)]
    while queue:
        now_x, now_y = queue.pop()
        for k in range(8):  # search 8 direction
            nx = now_x + direction_x[k]
            ny = now_y + direction_y[k]
            if 0 <= nx < w and 0 <= ny < h:  # search direction if it's out of range
                if array[ny][nx] == 1 and visited[ny][nx] == False:
                    visited[ny][nx] = True  # marked that point as visited
                    queue.append((nx, ny))  # append next position in queue
    return


while True:
    w, h = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(h)]  # make array size as w X h
    visited = [[False] * w for _ in range(h)]
    # setting data structures

    count = 0
    if w == 0 and h == 0:
        break
    # setting breakpoint

    for i in range(h):
        for j in range(w):
            if array[i][j] == 1 and visited[i][j] == False:  # if starting point is 1 , and not visited = execute bfs
                visited[i][j] = True
                count += 1  # if find island, add 1 on count
                bfs(j, i)
    print(count)
