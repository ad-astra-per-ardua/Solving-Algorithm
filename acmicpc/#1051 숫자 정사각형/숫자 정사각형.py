import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int ,input().strip())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        target = graph[i][j]
        for k in range(j, m):
            if graph[i][k] == target and i + k - j < n and k < m:
                if graph[i + k - j][j] == target and graph[i + k - j][k] == target:

                    answer.append((k - j + 1) ** 2)

print(max(answer))