import sys
input = sys.stdin.readline

direction_x = [1,0,-1,0]
direction_y = [0,1,0,-1]


def bfs(y,x):
    current = [(y,x)]
    graph[y][x] = 0
    while current:
        now_y, now_x = current.pop()
        for j in range(4):
            next_x = direction_x[j] + now_x
            next_y = direction_y[j] + now_y
            if 0 <= next_x < m and 0 <= next_y < n:
                if graph[next_y][next_x] == 1 and visited[next_y][next_x] == False:
                    current.append((next_y,next_x))
                    visited[next_y][next_x] = True
    return


loop = int(input())
for _ in range(loop):
    m,n,k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
    for i in range(n):
        for e in range(m):
            if graph[i][e] == 1 and visited[i][e] == False:
                count += 1
                bfs(i, e)

    print(count)