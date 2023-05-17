from collections import deque
import sys
sum1 = deque()
sum2 = deque()
ans1 = 0
ans2 = 0

for i in range(20):
    a = int(sys.stdin.readline())
    if i < 10:
        sum1.append(a)
    else:
        sum2.append(a)
sum1 = deque(sorted(sum1,reverse=True))
sum2 = deque(sorted(sum2,reverse=True))

for _ in range(3):
    ans1 += sum1.popleft()
    ans2 += sum2.popleft()
print(ans1,ans2)