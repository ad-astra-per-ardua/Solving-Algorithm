from collections import defaultdict

def dfs(start, n, edge_dict) :
    q = [(start, 0)]
    visited = [False]*(n+1)
    visited[start] = True
    max_node, max_dist, max_check = start, 0, 1
    
    while q :
        node, dist = q.pop()
        if dist > max_dist :
            max_node, max_dist, max_check = node, dist, 1
        elif dist == max_dist :
            max_check = 0
            
        for next_node in edge_dict[node] :
            if not visited[next_node] :
                visited[next_node] = True
                q.append((next_node, dist+1))
    
    return max_node, max_dist, max_check


def solution(n, edges):
    edge_dict = defaultdict(list)
    
    for a, b in edges :
        edge_dict[a].append(b)
        edge_dict[b].append(a)
    
    start_node, _, _ = dfs(1, n, edge_dict)
    end_node, diameter, check = dfs(start_node, n, edge_dict)
    if not check :
        return diameter
    
    _, diameter, check = dfs(end_node, n, edge_dict)
    return diameter-check