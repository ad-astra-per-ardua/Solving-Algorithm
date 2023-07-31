import sys

n = int(sys.stdin.readline())
hgt = list(map(int, sys.stdin.readline().split()))

stack = []
result = []

for i in range(n):
    while stack and stack[-1][0] <= hgt[i]:
        stack.pop()

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1])

    stack.append((hgt[i], i + 1))

for x in result:
    print(x, end=' ')
