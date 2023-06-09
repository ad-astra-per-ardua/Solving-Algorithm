from collections import deque
import sys
input = sys.stdin.readline
n = int(input().rstrip())

lists = deque(map(int,input().split()))
lists = deque(sorted(lists))
if len(lists) == 1:
    temp = lists.popleft()
    print(temp ** 2)
else:
    a = lists.pop()
    b = lists.popleft()
    print(a * b)
