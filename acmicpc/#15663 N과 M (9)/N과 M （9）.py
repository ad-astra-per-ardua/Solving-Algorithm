from itertools import permutations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

p = list(set(permutations(nums, M)))
p.sort()

for i in p:
    print(' '.join(map(str, i)))
