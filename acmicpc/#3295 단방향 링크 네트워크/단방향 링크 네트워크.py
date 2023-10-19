import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_000
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########
MAX = 1005

def DFS(from_, Left, Right, Visit, Adj):
    Visit[from_] = True
    for to in Adj[from_]:
        if Right[to] == -1 or (not Visit[Right[to]] and DFS(Right[to], Left, Right, Visit, Adj)):
            Left[from_] = to
            Right[to] = from_
            return True
    return False

def main():
    T = int(input())
    for _ in range(T):
        Adj = [[] for _ in range(MAX)]

        N, M = map(int, input().split())
        for _ in range(M):
            from_, to = map(int, input().split())
            Adj[from_].append(to)

        match = 0
        Left, Right = [-1]*MAX, [-1]*MAX
        for i in range(N):
            Visit = [False]*MAX
            if DFS(i, Left, Right, Visit, Adj):
                match += 1

        print(match)

if __name__ == "__main__":
    main()
