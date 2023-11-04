import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**5)
input = lambda: stdin.readline().strip()

######### main code goes here #########
from collections import deque

n = int(input())
d = deque(x for x in range(n, 0 ,-1))

while len(d) > 1:
	d.pop()
	temp = d.pop()
	d.appendleft(temp)
print(*d)
