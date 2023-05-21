import sys
from collections import deque
input = sys.stdin.readline

loop = int(input())

for _ in range(loop):
    case = deque(map(int, input().split()))
    length = case.popleft()
    case = sorted(case)
    avg = sum(case) // length
    standard = tuple(case)
    for i in standard:
        if i <= avg:
            case.remove(i)
        else:
            ans = round((len(case) / length) * 100,3)
    if len(case) == 0:
        ans = 0
    print(f"{ans:.3f}%")