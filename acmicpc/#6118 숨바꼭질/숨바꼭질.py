import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)

queue = [[1, 0]]
visited = [False]*(n+1)
result = []

while queue:
    cur_node, current = queue.pop(0)
    visited[cur_node] = True

    leaf = True
    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            leaf = False
            queue.append([next_node, current + 1])
            visited[next_node] = True
    if leaf:
        result.append([current, cur_node])

result.sort(key=lambda x:(-x[0], x[1]))
cost, min_node = result[0]
cnt = 0
for current, node in result:
    if cost != current: break
    cnt += 1

print(f"{min_node} {cost} {cnt}")