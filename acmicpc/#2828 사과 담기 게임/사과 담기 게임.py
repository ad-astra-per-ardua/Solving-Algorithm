from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())

q = deque()
for i in range(n):
    q.append(1) if i<m else q.append(0)

def solve(d):
    if q[c-1] == 1:
        return 0
    else:
        q.rotate(d)
        return 1 + solve(d)

temp1 = 1
result = 0
for _ in range(j):
    c = int(input())
    if temp1 < c:
        result += solve(1)
    else:
        result += solve(-1)
    temp1 = c

print(result)