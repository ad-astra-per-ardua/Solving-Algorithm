import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

m = min(a)
for x in a:
    if m < x < 2 * m:
        print(m // 2)
        exit(0)
print(m)
