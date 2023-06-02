import sys
input = sys.stdin.readline

loop = int(input())
tips = []
summation = 0
for _ in range(loop):
    a = int(input())
    tips.append(a)
tips = sorted(tips,reverse=True)

for i in range(len(tips)):
    actual_tip = tips[i] - ((i+1) - 1)
    if actual_tip < 0:
        actual_tip = 0
    summation += actual_tip
print(summation)