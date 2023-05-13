import math,sys
input = sys.stdin.readline
loop = int(input())
temp = 0
lists = list(map(int,input().split()))
for i in lists:
    if i == 1:
        continue
    for e in range(2, i):
        if i % e == 0:
            break
    else:
        temp += 1

print(temp)
