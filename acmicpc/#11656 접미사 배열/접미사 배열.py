from collections import deque
import sys
input = sys.stdin.readline

lists = deque(input().rstrip())
popped = deque()
for _ in range(len(lists)):
    popped.append("".join(lists))
    lists.popleft()
popped = sorted(popped)

for i in popped:
    print(i)