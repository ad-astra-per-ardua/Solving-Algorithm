from collections import deque
import sys
input = sys.stdin.readline

loop = int(input())
house = deque()
for _ in range(loop):
    s = input().split()
    if s[0] == 'push':
        house.append(s[1])
    elif s[0] == 'pop':
        if not house:
            print(-1)
        else:
            print(house.popleft())
    elif s[0] == 'size':
        print(len(house))
    elif s[0] == 'empty':
        if not house:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not house:
            print(-1)
        else:
            print(house[0])
    elif s[0] == 'back':
        if not house:
            print(-1)
        else:
            print(house[-1])