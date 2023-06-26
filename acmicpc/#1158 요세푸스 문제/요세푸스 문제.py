from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

lists = deque()
for i in range(n,0,-1):
    lists.append(i)
output = []

while lists:
    lists.rotate(k)
    temp = lists.popleft()
    output.append(temp)

answer = ', '.join(map(str, output))
print(f"<{answer}>")