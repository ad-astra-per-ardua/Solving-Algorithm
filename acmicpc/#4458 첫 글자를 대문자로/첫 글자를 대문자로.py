from collections import deque
loop = int(input())

for _ in range(loop):
    string = deque(input())
    temp = string.popleft()
    temp2 = temp.upper()
    string.appendleft(temp2)
    print(''.join(map(str,string)))