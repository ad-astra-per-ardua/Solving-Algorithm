from collections import deque
import sys
input = sys.stdin.readline

def bfs(t):
    queue = deque([t])
    while queue:
        t = queue.popleft()
        if t == k:
            return array[t]
        for nv in (t-1, t+1, 2*t):
            if 0 <= nv < 100001 and not array[nv]:
                array[nv] = array[t] + 1
                queue.append(nv)


n,k = map(int,input().split())
array = [0] * 100001
print(bfs(n))