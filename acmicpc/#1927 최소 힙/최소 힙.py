import heapq as hp
import sys
input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    try:
        integer = int(input())  # if n is int = heappush, n is 0 = heappop and if is in nothing, print 0
        if integer == 0:
            print(hp.heappop(heap))
        else:
            hp.heappush(heap,integer)
    except IndexError:
        print(0)
        continue
