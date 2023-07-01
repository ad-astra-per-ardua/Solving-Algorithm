import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))
d = deque()
for i in range(n):
    d.append((array[i], i + 1))
result = []

first, idx = d.popleft()
result.append(idx)

for i in range(n-1):
    if first > 0:
        for j in range(first -1):
            x = d.popleft()
            d.append(x)
    else:
        for j in range(-first):
            x = d.pop()
            d.appendleft(x)
    first, idx = d.popleft()
    result.append(idx)

print(*result)