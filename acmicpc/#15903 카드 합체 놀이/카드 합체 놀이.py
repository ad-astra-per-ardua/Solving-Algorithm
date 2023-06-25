import heapq as hq
import sys
input = sys.stdin.readline

loop, combine = map(int,input().split())
card = list(map(int,input().split()))

hq.heapify(card)

for i in range(combine):
    card1 = hq.heappop(card)
    card2 = hq.heappop(card)
    summation = card1 + card2
    hq.heappush(card, summation)
    hq.heappush(card, summation)
print(sum(card))