from collections import deque
import sys
input = sys.stdin.readline

loop = int(input())

for i in range(loop):
    rev = 0
    flag = 0
    func = list(input())
    discard = int(input())
    array = deque(input()[1:-2].split(","))
    if discard == 0:
        array = []
    for e in func:
        if e == 'R':
            rev += 1
        elif e == 'D':
            if len(array) < 1:
                flag = 1
                print('error')
                break
            else:
                if rev % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(array) + "]")
        else:
            array.reverse()
            print("[" + ",".join(array) + "]")
