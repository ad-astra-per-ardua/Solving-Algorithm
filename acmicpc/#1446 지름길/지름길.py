import sys
import heapq as hq
input = sys.stdin.readline

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]

for i in range(D):
    graph[i].append((i+1, 1))

for i in range(N):
    start, end, length = map(int, input().split())
    if end > D: continue
    graph[start].append((end, length))

INF = 987654321
dist = [INF]*(D+1)
dist[0] = 0

q = []
hq.heappush(q, (0, 0))
while q:
    d, now = hq.heappop(q)
    if dist[now] < d: continue

    for x in graph[now]:
        cost = d + x[1]

        if dist[x[0]] > cost:
            dist[x[0]] = cost
            hq.heappush(q, (cost, x[0]))

print(dist[D])