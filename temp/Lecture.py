import sys
input = sys.stdin.readline

n = int(input())
ans = n * (n + 1) // 2
for i in input().split():
    ans -= int(i)
print(ans)
