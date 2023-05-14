from collections import deque
import sys
loop = int(sys.stdin.readline().strip())
for _ in range(loop):
    blank = sys.stdin.readline().strip()
    stack = deque()
    for i in blank:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print('NO')
                break
            stack.pop()
    else:
        if stack:
            print('NO')
        else:
            print('YES')
