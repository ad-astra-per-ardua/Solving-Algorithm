from collections import deque
import sys
input = sys.stdin.readline
n, l = map(int,input().split())
fruit = deque(map(int,input().split()))

fruit = sorted(fruit)
for i in range(n):
    if l >= fruit[i]:
        l += 1
    else:
        print(l)
        exit(0)
print(l)