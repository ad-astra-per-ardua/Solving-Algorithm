import sys
input = sys.stdin.readline
n = int(input())
stage = []
diff = 0
for _ in range(n):
    stage.append(int(input()))
stage.reverse()

for i in range(1,len(stage)):
    if stage[i-1] < stage[i]:
        diff += stage[i] - stage[i-1] + 1
        stage[i] = stage[i-1] - 1
    elif stage[i-1] == stage[i]:
        diff += 1
        stage[i] = stage[i-1] - 1

print(diff)