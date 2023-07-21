import sys
input = sys.stdin.readline

array = [[0] * 100 for _ in range(101)]
count = 0

for _ in range(4):
    a,b,x,y = map(int,input().split())
    for e in range(a,x):
        for t in range(b,y):
            if array[e][t] == 0:
                array[e][t] += 1
                count += 1
print(count)