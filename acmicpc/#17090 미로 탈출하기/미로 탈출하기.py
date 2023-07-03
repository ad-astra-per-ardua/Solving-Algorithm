import sys
sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return True
    if visited[x][y]:
        return dp[x][y]
    visited[x][y] = True
    dp[x][y] = dfs(x + dx[board[x][y]], y + dy[board[x][y]])
    return dp[x][y]

n, m = map(int, sys.stdin.readline().split())
board = [list(map('URDL'.index, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dp = [[False]*m for _ in range(n)]

answer = sum(dfs(i, j) for i in range(n) for j in range(m))
print(answer)
