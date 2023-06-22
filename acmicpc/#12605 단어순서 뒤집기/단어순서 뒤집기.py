import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    words = input().split()
    stack = []
    for word in words:
        stack.append(word)

    reverse = []
    while stack:
        reverse.append(stack.pop())

    print(f"Case #{i+1}:",' '.join(reverse))
