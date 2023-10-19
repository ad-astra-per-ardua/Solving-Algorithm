import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from bisect import bisect_left, bisect_right
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_000
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

MAX = 360000


def getpi(pattern):
    pi = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


def kmp(text, pattern):
    pi = getpi(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == len(pattern) - 1:
                return "possible"
            else:
                j += 1
    return "impossible"


if __name__ == "__main__":
    n = int(input())

    clock1 = [0] * (2 * MAX)
    clock2 = [0] * MAX

    nums = list(map(int, input().split()))
    for num in nums:
        clock1[num] = clock1[MAX + num] = 1

    nums = list(map(int, input().split()))
    for num in nums:
        clock2[num] = 1

    print(kmp(clock1, clock2))
