from collections import deque
import sys
input = sys.stdin.readline

temp = deque()
n = int(input())
for i in range(n):
    temp.append(int(input()))
temp = deque(sorted(temp))
for e in range(len(temp)):
    print(temp.popleft())