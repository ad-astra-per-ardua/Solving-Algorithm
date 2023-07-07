from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def bfs(k, v):
    visited = [0] * (N + 1)
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 0
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i[0]]:
                if i[1] >= k:
                    q.append(i[0])
                    cnt += 1
                    visited[i[0]] = 1
    return cnt


if __name__ == "__main__":
    N, Q = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    for _ in range(Q):
        k, v = map(int, input().split())
        print(bfs(k, v))