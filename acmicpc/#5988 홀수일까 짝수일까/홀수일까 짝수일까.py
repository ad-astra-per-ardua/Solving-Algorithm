import sys
input = sys.stdin.readline
loop = int(input())

for _ in range(loop):
    integer = list(map(int,input().split()))
    if integer[-1] % 2 == 0:
        print('even')
    else:
        print('odd')