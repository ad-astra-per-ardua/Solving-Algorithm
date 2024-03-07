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

def kmp(word):
    pi = [0] * (len(word) + 5)
    pIdx = 0
    for idx in range(1, len(word)):
        while word[idx] != word[pIdx] and pIdx > 0:
            pIdx = pi[pIdx - 1]
        if word[idx] == word[pIdx]:
            pIdx += 1
            pi[idx] = pIdx

    if pi[len(word) - 1] % (len(word) - pi[len(word) - 1]) != 0:
        if K == 1:
            return 1
        else:
            return 0

    return 1 if K - 1 == pi[len(word) - 1] // (len(word) - pi[len(word) - 1]) else 0


def getComb(word, words, check):
    if len(word) == size:
        return kmp(word)
    ret = 0
    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        ret += getComb(word + words[i], words, check)
        check[i] = False
    return ret


if __name__ == "__main__":
    N = int(input())
    words = [input() for _ in range(N)]
    size = sum(len(word) for word in words)
    K = int(input())

    check = [False] * (N + 5)
    print(getComb("", words, check))
