from itertools import combinations
from collections import *
import sys, copy
input = sys.stdin.readline

safe = []
hazard = []
ans = 0
direction_x = [-1, 0, 1, 0]
direction_y = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(temp):
    global ans
    count = len(safe) - 3
    array = deque([])
    for x, y in hazard:
        array.append((x, y))
    while array:
        nowx, nowy = array.popleft()
        for i in range(4):
            nextx = nowx + direction_x[i]
            nexty = nowy + direction_y[i]
            if 0 <= nextx<n and 0 <= nexty<m and temp[nextx][nexty] == 0:
                temp[nextx][nexty] = 2
                array.append((nextx, nexty))
                count -= 1
    ans = max(ans, count)



for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safe.append((i,j))
        elif graph[i][j] == 2:
            hazard.append((i,j))

for com in combinations(safe,3):
    temp = copy.deepcopy(graph)
    for x,y in com:
        temp[x][y] = 1
    bfs(temp)
print(ans)
