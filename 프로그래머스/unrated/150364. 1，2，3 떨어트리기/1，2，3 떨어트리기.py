from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def solution(edges, target):
    adjacency = defaultdict(list)
    tree = defaultdict(list)
    visited = [False]*len(target)
    visited[0] = True
    
    for parent, child in edges:
        adjacency[parent-1].append(child-1)
        adjacency[child-1].append(parent-1)

    def dfs(node):
        children = [child for child in adjacency[node] if not visited[child]]
        for child in children:
            visited[child] = True
        if not children:
            return [node]
        tree[node].extend([0, sorted(children)])
        leaf_nodes = [dfs(child) for child in children]
        return [node for sublist in leaf_nodes for node in sublist]

    def find_leaf(node):
        if not tree[node]:
            return node
        index = tree[node][0]
        tree[node][0] = (tree[node][0] + 1) % len(tree[node][1])
        return find_leaf(tree[node][1][index])

    leaf_nodes = dfs(0)
    leaf_count = {node: 0 for node in leaf_nodes}
    target_reached = {node: target[node] == 0 for node in leaf_nodes}
    visited_order = []

    while not all(target_reached.values()):
        current_node = find_leaf(0)
        leaf_count[current_node] += 1

        if leaf_count[current_node] > target[current_node]:
            return [-1]
        if not target_reached[current_node] and leaf_count[current_node]*3 >= target[current_node]:
            target_reached[current_node] = True
        visited_order.append(current_node)

    answer = [0]*len(visited_order)
    for node in leaf_nodes:
        remaining = target[node] - leaf_count[node]
        node_result = [1]*(leaf_count[node] - remaining % 2 - remaining // 2) + [2]*(remaining % 2) + [3]*(remaining // 2)

        for index, visited_node in enumerate(visited_order):
            if visited_node == node:
                answer[index] = node_result.pop(0)

    return answer
