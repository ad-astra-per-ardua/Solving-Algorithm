import math,heapq,sys
input = sys.stdin.readline

point = []
heap = []

def square(a):
    return a*a

def cal(a, b):
    return math.sqrt(square(point[b][0] - point[a][0]) + square(point[b][1] - point[a][1]))

def find(count, visit, present, cost):
    if count == 3:
        heapq.heappush(heap, cost)
    else:
        for i in range(1, 4):
            if visit[i] == 0:
                visit[i] = 1
                find(count + 1, visit, i, cost + cal(present, i))
                visit[i] = 0

for _ in range(4):
    tempa, tempb = map(int, input().split())
    point.append((tempa, tempb))

visit = [0]*4
visit[0] = 1

find(0, visit, 0, 0)

print(int(heap[0]))
