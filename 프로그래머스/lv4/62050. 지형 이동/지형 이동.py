from collections import deque
import sys

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, num, land, height, visit):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = num
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(land) and ny < len(land):
                if visit[nx][ny] == 0 and abs(land[x][y] - land[nx][ny]) <= height:
                    visit[nx][ny] = num
                    queue.append((nx, ny))

def make_group(land, height, visit):
    group_cnt = 1
    for i in range(len(land)):
        for j in range(len(land[i])):
            if visit[i][j] == 0:
                bfs(i, j, group_cnt, land, height, visit)
                group_cnt += 1
    return group_cnt

def find_group_distance(land, visit):
    edge = []
    for x in range(len(land)):
        for y in range(len(land)):
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx >= 0 and ny >= 0 and nx < len(land) and ny < len(land):
                    if visit[x][y] != visit[nx][ny]:
                        edge.append((abs(land[x][y] - land[nx][ny]), (visit[x][y], visit[nx][ny])))
    return edge

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        parent[b] = a

def kruskal(edge, parent, group_cnt):
    edge.sort()
    answer = 0
    for i in range(group_cnt):
        parent[i] = i
    for cost, (n1, n2) in edge:
        if find_parent(parent, n1) != find_parent(parent, n2):
            union(parent, n1, n2)
            answer += cost
    return answer

def solution(land, height):
    N = len(land)
    visit = [[0]*N for _ in range(N)]
    group_cnt = make_group(land, height, visit)
    edge = find_group_distance(land, visit)
    parent = [0]*group_cnt
    return kruskal(edge, parent, group_cnt)
