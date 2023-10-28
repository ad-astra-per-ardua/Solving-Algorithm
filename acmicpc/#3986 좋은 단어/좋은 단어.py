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

def solve(txt):
    global count
    stack = []
    for i in txt:
    	if stack and stack[-1] == i:
    		stack.pop()
    	else:
    		stack.append(i)

    if stack:
    	count -= 1


if __name__ == '__main__':
	loop = int(input())
	count = loop
	for _ in range(loop):
		txt = input().rstrip()
		solve(txt)
	print(count)