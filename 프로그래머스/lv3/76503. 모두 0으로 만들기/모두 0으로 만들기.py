from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10**6)

def dfs(node, parent, b, adj):
    total = 0
    for child in adj[node]:
        if child != parent:
            total += dfs(child, node, b, adj)
    total += abs(b[node])
    b[parent] += b[node]
    return total

def solution(a, edges):
    n = len(a)
    b = a[:]
    adj = defaultdict(list)
    
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    answer = dfs(0, 0, b, adj)
    return answer if b[0] == 0 else -1
