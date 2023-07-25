import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

if sum(a-b) == 0:
    print(0)
else:
    print(len(a-b))
    print(*sorted(a-b))