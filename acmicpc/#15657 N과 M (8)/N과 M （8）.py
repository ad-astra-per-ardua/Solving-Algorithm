from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

for num in list(combinations_with_replacement(nums,m)):
    for i in num:
        print(i, end=' ')
    print()
