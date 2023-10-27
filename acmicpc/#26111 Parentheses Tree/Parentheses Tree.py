import sys
import time
from sys import stdin, stdout
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
def flush(): return stdout.flush()
def stdstr(): return stdin.readline()

mod = 10_0000_0007
sys.setrecursionlimit(1_0000_0000)
input = lambda: sys.stdin.readline().strip()
# main code goes here

str_ = input()
stack = []
l = -1
result = 0

for i, e in enumerate(str_):
    if e == '(':
        l = i
        stack.append(e)
    else:
        if l == i - 1:
            result += len(stack) - 1
        stack.pop()

print(result)
