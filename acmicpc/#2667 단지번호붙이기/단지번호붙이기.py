import sys
input = sys.stdin.readline

n = int(input().rstrip())
array = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []
separate = 0
direction_x = [1,0,-1,0]
direction_y = [0,1,0,-1]


def dfs(x, y):
    global separate
    separate += 1
    for k in range(4):
        next_y = y + direction_y[k]
        next_x = x + direction_x[k]
        if 0 <= next_x < n and 0 <= next_y < n:
            if array[next_x][next_y] == 1 and visited[next_x][next_y] == False:
                visited[next_x][next_y] = True
                dfs(next_x, next_y)


for i in range(n):
    for j in range(n):
        if array[i][j] == 1 and visited[i][j] == False:
            visited[i][j] = True
            separate = 0
            dfs(i,j)
            result.append(separate)

result.sort()
print(len(result))
for e in result:
    print(e)
