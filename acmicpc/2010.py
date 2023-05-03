import sys
n = int(sys.stdin.readline())
ans = 0
for i in range(n):
    p = int(sys.stdin.readline())
    ans += p

print(ans-(n-1))
