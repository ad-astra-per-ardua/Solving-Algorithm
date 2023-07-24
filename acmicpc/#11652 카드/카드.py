from collections import deque
import statistics,sys
input = sys.stdin.readline

loop = int(input())
deck = deque()
for _ in range(loop):
    deck.append(int(input()))

deck = sorted(deck)
ans = statistics.mode(deck)
print(ans)