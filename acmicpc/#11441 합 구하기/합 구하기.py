import sys
input = sys.stdin.readline

n = int(input())
array_n = list(map(int,input().split()))
loop = int(input())
for _ in range(loop):
    i, j = map(int,input().split())
    print(sum(array_n[i-1:j]))
