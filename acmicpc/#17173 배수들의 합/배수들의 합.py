from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = deque(map(int, input().split()))

temp = []
for j in k:
    for i in range(1,n+1):
        if i % j == 0:
            temp.append(i)

print(sum(set(temp)))
