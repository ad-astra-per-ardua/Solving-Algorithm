import sys,math,time
from itertools import permutations,combinations,combinations_with_replacement
from sys import stdin, stdout
from math import gcd, floor, sqrt, log, perm, comb
from collections import defaultdict,deque
from bisect import bisect_left as bl, bisect_right as br
from heapq import heapify, heappush, heappop
from functools import lru_cache, reduce
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
def flush(): return stdout.flush()
def stdstr(): return stdin.readline()

mod = 1_000_000_007
# sys.setrecursionlimit(100_000_000)
input = lambda: stdin.readline().strip()
# main code goes here

j1 = []
j2 = []

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]

def caseCheck(x1, x2, y1, y2):
    j1_count = 0
    j2_count = 0

    for i in range(len(j1)):
        if x1 <= j1[i][0] <= x2 and y1 <= j1[i][1] <= y2:
            j1_count += 1

    for i in range(len(j2)):
        if x1 <= j2[i][0] <= x2 and y1 <= j2[i][1] <= y2:
            j2_count += 1

    if j2_count - 1 > j1_count or j2_count == 0:
        return 0

    if j1_count == 0 and j2_count == 1:
        return 1

    return 2

def solve(x1, x2, y1, y2, flag):
    check = caseCheck(x1, x2, y1, y2)
    if check == 0:
        return 0
    elif check == 1:
        return 1

    temp = 0
    if flag:
        for i in range(x1 + 1, x2):
            f = False
            for j in range(y1, y2 + 1):
                if graph[i][j] != 0:
                    if graph[i][j] == 2:
                        f = False
                        break
                    else:
                        f = True
            if f:
                temp += solve(x1, i - 1, y1, y2, 0) * solve(i + 1, x2, y1, y2, 0)
    else:
        for i in range(y1 + 1, y2):
            f = False
            for j in range(x1, x2 + 1):
                if graph[j][i] != 0:
                    if graph[j][i] == 2:
                        f = False
                        break
                    else:
                        f = True
            if f:
                temp += solve(x1, x2, y1, i - 1, 1) * solve(x1, x2, i + 1, y2, 1)

    return temp

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = row[j]
        if graph[i][j] == 1:
            j1.append((i, j))
        elif graph[i][j] == 2:
            j2.append((i, j))

result = solve(0, n - 1, 0, n - 1, 0) + solve(0, n - 1, 0, n - 1, 1)

if result:
    print(result)
else:
    print(-1)
