import sys
input = sys.stdin.readline
count = 0
N, M = map(int, input().split())
s = set()
for _ in range(N):
    s.add(input().rstrip())
for _ in range(M):
    checker = set(input().rsplit())
    if set(checker) & s:
        count += 1

print(count)