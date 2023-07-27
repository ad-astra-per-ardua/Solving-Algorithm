import sys
input = sys.stdin.readline

N = int(input())
pointX = [0]*(N+1)
pointY = [0]*(N+1)
countY = [0]*111111
countX = [0]*111111

for i in range(1, N+1):
    x, y = map(int, input().split())
    pointX[i] = x
    pointY[i] = y
    countY[y] += 1
    countX[x] += 1

sum = 0
for a in range(1, N+1):
    if countY[pointY[a]] > 1 and countX[pointX[a]] > 1:
        sum += (countY[pointY[a]] - 1) * (countX[pointX[a]] - 1)

print(sum)
