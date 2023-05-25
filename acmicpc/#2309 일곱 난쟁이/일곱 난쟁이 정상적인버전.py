import sys
import itertools

heights = [int(sys.stdin.readline()) for _ in range(9)]

for combination in itertools.combinations(heights, 7):
    if sum(combination) == 100:
        for height in sorted(combination):
            print(height)
        break
