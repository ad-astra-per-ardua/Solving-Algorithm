from itertools import combinations, permutations
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]

numbers = set()

for comb in combinations(cards, k):
    for perm in permutations(comb):
        numbers.add(int(''.join(perm)))

print(len(numbers))
