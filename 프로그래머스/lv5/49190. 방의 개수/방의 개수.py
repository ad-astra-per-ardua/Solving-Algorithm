dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(arrows):
    node = set()
    edge = set()

    x, y = 0, 0
    node.add((x, y))

    for i in arrows:
        for _ in range(2):
            nx, ny = x + dx[i], y + dy[i]
            node.add((nx, ny))
            edge.add(((min(x, nx), min(y, ny)), (max(x, nx), max(y, ny))))
            x, y = nx, ny
            
    return len(edge) - len(node) + 1
