from collections import deque
import sys,itertools
input = sys.stdin.readline

n = int(input().rstrip())
lists = list(map(int,input().split()))
target = int(input().rstrip())
count = 0
lists.sort()

for i in range(n):
    for j in range(i+1,n):
        if lists[i] + lists[j] == target:
            count += 1
        if lists[i] + lists[j] > target:
            break
print(count)