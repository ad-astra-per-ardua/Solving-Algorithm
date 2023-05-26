import sys
from collections import deque
input = sys.stdin.readline

integer = deque()
loop = int(input())
for i in range(loop):
    integer.append(int(input()))
integer = sorted(integer)
for e in range(len(integer)):
    print(integer.pop())