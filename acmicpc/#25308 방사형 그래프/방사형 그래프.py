from itertools import permutations
from math import sqrt
import sys
input = sys.stdin.readline


def check(v):
    for i in range(8):
        a, b, c = v[i], v[(i + 1) % 8], v[(i + 2) % 8]
        if a * c * sqrt(2) > b * (a + c):
            return False
    return True


a = list(map(int, input().split()))[:8]
ans = sum(check(v) for v in permutations(a))

print(ans)
