import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    print(i, end=' ')
    if i in a[:2]:
        print(1)
    elif i in a[2:]:
        print(-1)
    else:
        print(0)

print(n, end=' ')

temp = 10 ** 9
if n in a[:2]:
    print(temp)
else:
    print(-temp)
