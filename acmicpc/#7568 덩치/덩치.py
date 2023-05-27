import sys
input = sys.stdin.readline
loop = int(input())
info = []
for _ in range(loop):
    a,b = list(map(int,input().split()))
    info.append((a,b))
for i in info:
    rank = 1
    for e in info:
        if i[0] < e[0] and i[1] < e[1]:
            rank += 1
    print(rank,end=" ")
