from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
dq = deque()

for i in range(n, 0, -1):
    dq.appendleft(i)
    for e in range(i):
        dq.appendleft(dq.pop())

print(*dq)
