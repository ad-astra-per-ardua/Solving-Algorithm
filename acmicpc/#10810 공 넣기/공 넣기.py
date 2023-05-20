import sys
input = sys.stdin.readline
n, m = map(int, input().split())
box = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int,input().split())
    for i in range(a,b+1):
        box[i] = c
print(*box[1:n+1])