import sys,math
from sys import stdin, setrecursionlimit
import heapq
from types import GeneratorType
def lcm(x, y):
    return x * y // math.gcd(x, y)
def perm(n, r):
    return math.factorial(n) // math.factorial(n-r)
def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
# Set direction for graph traversal DFS,BFS Etc... 
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########
n = int(input())
k = int(input())

start, end = 0, k

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in range(1, n + 1):
        count += min(mid // i, n)

    if count >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
print(answer)