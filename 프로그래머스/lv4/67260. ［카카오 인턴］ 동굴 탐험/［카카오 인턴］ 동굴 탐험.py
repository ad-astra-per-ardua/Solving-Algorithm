from collections import deque
def solution(n, path, order):
    answer = True
    graph = {n:[] for n in range(n)}
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    precedeA = {}
    precedeB = {}

    for a, b in order:
        precedeA[a] = b
        precedeB[b] = a
        if b == 0:
            return False
        if a == 0:
            precedeA[0] = 0

    visited = [0] * n
    visited[0] = 1

    q = deque()
    q.append(0)

    while q:
        now = q.popleft()
        if now == precedeA.get(precedeB.get(now)):
            visited[now] = 2
        else:
            for x in graph[now]:
                if visited[x] == 0:
                    q.append(x)
                    visited[x] = 1

                    if precedeA.get(x): 
                        if visited[precedeA[x]] == 2: 
                            q.append(precedeA[x])
                            visited[precedeA[x]] = 1
                        precedeA[x] = 0
    for i in visited:
        if i == 0:
            return False
    return answer