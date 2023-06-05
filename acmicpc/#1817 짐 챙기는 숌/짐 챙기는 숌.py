from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
if n == 0:
    print(0)
    exit(0)
array = deque(list(map(int, input().split())))
weight = 0
count = 1
for i in array:
    if i + weight > m:
        count += 1
        weight = 0
    weight += i

print(count)