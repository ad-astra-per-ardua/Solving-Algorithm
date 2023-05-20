import sys,math
from collections import deque
input = sys.stdin.readline

fin_score = deque()
prob = int(input().rstrip())
score = deque(map(int,input().split()))
copy = tuple(score)
for i in copy:
    temp = score.popleft()
    temp2 = temp / max(copy) * 100
    fin_score.append(temp2)
avg = sum(fin_score) / len(fin_score)
print(avg)