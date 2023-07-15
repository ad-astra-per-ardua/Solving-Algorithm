import sys
input = sys.stdin.readline
a, b, n = map(int, input().split())
a *= 10 ** n
ans = a // b % 10
print(ans)
