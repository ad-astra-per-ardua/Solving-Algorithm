import heapq
import sys
from collections import deque

def solve():
    N, L = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))

    D = deque()
    Q = []

    for i in range(N):
        while D and D[0][1] < i - L + 1:
            D.popleft()

        while Q and Q[0][1] < i - L + 1:
            heapq.heappop(Q)

        heapq.heappush(Q, (A[i], i))
        while D and D[-1][0] > Q[0][0]:
            D.pop()

        D.append(Q[0])

        print(D[0][0], end=' ')

solve()
