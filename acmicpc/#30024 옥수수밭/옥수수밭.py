import heapq
import sys

N, M = map(int, sys.stdin.readline().split())

map_info = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

que = []
v = [[False] * M for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0 or i == N - 1 or j == M - 1:
            heapq.heappush(que, (-map_info[i][j], i, j))
            v[i][j] = True

K = int(sys.stdin.readline())

sb = []

while K > 0:
    cur_val, r, c = heapq.heappop(que)
    cur_val *= -1

    sb.append(f"{r + 1} {c + 1}\n")
    K -= 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc]:
            v[nr][nc] = True
            heapq.heappush(que, (-map_info[nr][nc], nr, nc))

sys.stdout.write("".join(sb))
