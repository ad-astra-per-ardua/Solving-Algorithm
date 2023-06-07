import sys
input = sys.stdin.readline

a = int(input().rstrip())
cnt = 0
while a != 0:
    if a % 2 == 1:
        cnt += 1
    a = a // 2
print(cnt)