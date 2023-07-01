from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DNA = [input().strip() for _ in range(N)]

small = ''
count = 0

for i in range(M):
    strings = defaultdict(int)

    for j in range(N):
        strings[DNA[j][i]] += 1

    maximum = max(('A', 'C', 'G', 'T'), key=lambda x: (strings[x], -ord(x)))
    small += maximum
    count += N - strings[maximum]

print(small)
print(count)
