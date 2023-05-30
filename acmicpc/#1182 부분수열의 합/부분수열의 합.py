from itertools import combinations
import sys

input = sys.stdin.readline


def solving_combination(subsequence, target):
    count = 0
    for i in range(1, len(subsequence)+1):
        for temp in combinations(subsequence, i):
            if sum(temp) == target:
                count += 1
    return count


n, target = map(int, input().split())
subsequence = list(map(int, input().split()))

answer = solving_combination(subsequence, target)
print(answer)
