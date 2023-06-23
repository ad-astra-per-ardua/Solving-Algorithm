from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
hand = deque()
floor = []
for e in range(n, 0, -1):
    floor.append(e)
command = list(map(int,input().split()))
command.reverse()

for i in command:
    if i == 1:
        hand.appendleft(floor.pop())
    elif i == 2:
        hand.insert(1,floor.pop())
    elif i == 3:
        hand.append(floor.pop())
print(*hand)
