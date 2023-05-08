from typing import List
import sys
from collections import deque

def solve(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    def dfs(i, j):
        queue = deque([(i, j)])
        volume = 0
        while queue:
            i, j = queue.popleft()
            if not visited[i][j]:
                visited[i][j] = True
                if grid[i][j] == 0:
                    continue
                volume += grid[i][j]
                for ni, nj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                        queue.append((ni, nj))
        return volume

    max_lake_volume = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                max_lake_volume = max(max_lake_volume, dfs(i, j))

    return max_lake_volume

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int,sys.stdin.readline().split())
    grid = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    print(solve(grid))
