import sys
input = sys.stdin.readline
num = list(input())
if "0" not in num:
    print(-1)
    exit(0)
num = sorted(num,reverse=True)
ans = ''.join(map(str,num))
if int(ans) % 30 != 0:
    print(-1)
else:
    print(int(ans))