from collections import deque
import math,sys
input = sys.stdin.readline

n = int(input())
discard_list = deque()
queue = deque(x for x in range(n,0,-1))
for _ in range(math.ceil(n-1)):  #   pop , pop+appendleft
    discard = queue.pop()
    discard_list.append(discard)
    shuffle = queue.pop()
    queue.appendleft(shuffle)
final = queue.pop()
discard_list.append(final)

print(*discard_list)