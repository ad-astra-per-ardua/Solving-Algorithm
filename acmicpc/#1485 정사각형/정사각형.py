import sys

def distance(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

T = int(sys.stdin.readline())
for _ in range(T):
    points = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
    dists = []
    for i in range(3):
        for j in range(i+1, 4):
            dists.append(distance(points[i][0], points[i][1], points[j][0], points[j][1]))
    dists.sort()
    if dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]:
        print(1)
    else:
        print(0)
