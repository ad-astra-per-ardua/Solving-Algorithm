import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())

lists = [list(map(int, input().split())) for _ in range(n)]
lists.sort()
queue = []

hq.heappush(queue, lists[0][1])

for i in range(1, n):
    if lists[i][0] < queue[0]:
        hq.heappush(queue, lists[i][1])
    else:
        hq.heappop(queue)
        hq.heappush(queue, lists[i][1])

print(len(queue))