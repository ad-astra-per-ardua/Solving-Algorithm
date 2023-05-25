import sys
import math

input = sys.stdin.readline
pools = []
n, l = map(int, input().split())
for _ in range(n):
    p = list(map(int,input().split()))
    pools.append(p)
pools.sort()

planks = 0
end = 0

for pool in pools:
    a, b = pool
    if end < a:
        end = a
    planks += math.ceil((b - end) / l)
    end += l * math.ceil((b - end) / l)

print(planks)
