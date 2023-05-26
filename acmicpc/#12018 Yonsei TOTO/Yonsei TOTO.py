import heapq,sys
input = sys.stdin.readline

n, m = map(int, input().split())
sub = []
for _ in range(n):
    p, l = map(int, input().split())
    point = list(map(int, input().split()))
    point.sort()
    if p < l:
        sub.append(1)
    else:
        sub.append(point[-l])
sub.sort()

count = 0
for i in range(n):
    if m >= sub[i]:
        m -= sub[i]
        count += 1
    else:
        break
print(count)
