import heapq as hp
import sys
input = sys.stdin.readline

heap = []
n = int(input().rstrip())

for _ in range(n):
    try:
        integer = int(input().rstrip())  # if n is int = heappush, n is 0 = heappop and if is in nothing, print 0
        if integer == 0:
            print(hp.heappop(heap)[1])
        else:
            hp.heappush(heap,(abs(integer),integer))
    except IndexError:
        print(0)
        continue
