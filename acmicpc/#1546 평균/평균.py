import sys
input = sys.stdin.readline

prob = int(input().rstrip())
scores = list(map(int, input().split()))
max_score = max(scores)
avg = sum((s / max_score * 100 for s in scores)) / prob
print(avg)
