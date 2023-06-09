import sys,itertools
input = sys.stdin.readline

loop = int(input().rstrip())

for _ in range(loop):
    m = int(input().rstrip())
    test = set(map(int,input().split()))
    m = int(input().rstrip())
    test1 = list(map(int,input().split()))
    for i in test1:
        if i in test:
            print(1)
        else:
            print(0)