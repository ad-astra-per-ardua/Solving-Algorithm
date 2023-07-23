import sys,math
from collections import defaultdict
input = sys.stdin.readline

def euclidean(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


N = int(input().rstrip())

signals = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    signals[x].append(y)

for v in signals.values():
    v.sort()

dx, dy = sorted(signals.items())[0]
high = low = 0
for nx, ny in sorted(signals.items())[1:]:
    high, low = max(high + euclidean(dx, max(dy), nx, max(ny)), low + euclidean(dx, min(dy), nx, max(ny))), \
                max(high + euclidean(dx, max(dy), nx, min(ny)), low + euclidean(dx, min(dy), nx, min(ny)))
    dx, dy = nx, ny

print("%.7f" % max(high, low))
