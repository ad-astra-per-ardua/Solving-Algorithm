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
# 기본세팅

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
# safe(0)와 hazard(2)부분의 좌표를 각각의 리스트에 저장


for com in combinations(safe,3):
    temp = copy.deepcopy(graph)
    for x,y in com:
        temp[x][y] = 1
    bfs(temp)

# 이후 조합을 이용해 safe 리스트에서 3개의 원소를 선택하는 모든조합을 생성
# 각 조합에 대해 deepcopy를 사용해서 복사된 행렬에 벽(1)을 세우고 그다음 2를 퍼뜨린후
# ans = max(ans, count)로 max값을 뽑아낸뒤 답을 출력

print(ans)
