from collections import deque
import sys
input = sys.stdin.readline
n,m,r = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)


def bfs(graph, start, visited):
	q = deque([start])
	visited[start] = 1
	count = 2
	while q:
		value = q.popleft()
		for j in graph[value]:
			if not visited[j]:
				q.append(j)
				visited[j] = count
				count += 1


for i in range(m):
	a, b = (map(int, input().split()))
	graph[a].append(b)
	graph[b].append(a)
for i in range(n+1):
	graph[i].sort()
bfs(graph, r, visited)
for i in range(1, n+1):
	print(visited[i])