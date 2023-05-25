import sys
input = sys.stdin.readline
n = int(input())
p = list(map(int,input().split()))
summation = 0
p.sort()
for i in range(len(p)):
    for j in range(1):
        summation += p[i] + sum(p[0:i])
print(summation)