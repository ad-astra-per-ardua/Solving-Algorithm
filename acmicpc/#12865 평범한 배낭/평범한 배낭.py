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

n,k = map(int, input().split())
put = [[1, 1]]
bag = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
    put.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        kg = put[i][0]
        val = put[i][1]

        if j < kg:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(val + bag[i - 1][j - kg], bag[i - 1][j])

print(bag[n][k])