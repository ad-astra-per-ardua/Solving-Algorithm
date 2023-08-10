import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def tarjan_dfs(v):
    global scc_id, vertex_id
    vertex_id += 1
    id[v] = vertex_id
    stack.append(v)

    parent = id[v]
    for to in graph[v]:
        if id[to] == 0:
            parent = min(parent, tarjan_dfs(to))
        elif not finished[to]:
            parent = min(parent, id[to])

    if parent == id[v]:
        scc = []
        while True:
            top = stack.pop()
            scc.append(top)
            finished[top] = True
            if top == v:
                break
        scc_list.append(scc)

    return parent


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)

id = [0] * (V + 1)
stack = []
scc_list = []
finished = [False] * (V + 1)

scc_id = 0
vertex_id = 0

for i in range(1, V + 1):
    if id[i] == 0:
        tarjan_dfs(i)

print(len(scc_list))
for scc in sorted(scc_list, key=lambda x: min(x)):
    scc_sorted = sorted(scc)
    print(*scc_sorted, -1)
