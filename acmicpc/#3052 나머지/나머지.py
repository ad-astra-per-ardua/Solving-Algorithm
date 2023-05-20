from collections import deque
import sys
input = sys.stdin.readline

temp = deque()
for _ in range(10):
    b = int(input().rstrip())
    add = b % 42
    temp.append(add)
ans = set(temp)
print(len(ans))
