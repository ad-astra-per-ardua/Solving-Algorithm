import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1
def stdstr(): return stdin.readline()

MOD = 1_000_000_007
setrecursionlimit(10**5)
# input = lambda: stdin.readline().strip()

######### main code goes here #########

from collections import defaultdict

MAX_N = 10001
MAX_M = 100000

N, M = 0, 0
Path = defaultdict(list)
id = 0
sccNum = 0
scc_id = [0] * (2 * MAX_N)
scc_finished = [0] * (2 * MAX_N)
sn = [0] * (2 * MAX_N)
scc_stack = []

def Not(a):
    if a > 0:
        return a + N
    else:
        return -a

def dfs(c):
    global id, sccNum
    scc_id[c] = id = id + 1
    scc_stack.append(c)
    res = scc_id[c]
    for next in Path[c]:
        if scc_id[next] == 0:
            res = min(res, dfs(next))
        elif not scc_finished[next]:
            res = min(res, scc_id[next])
    if res == scc_id[c]:
        while True:
            t = scc_stack.pop()
            scc_finished[t] = 1
            sn[t] = sccNum
            if t == c:
                break
        sccNum += 1
    return res

def Check():
    for i in range(1, N + 1):
        if sn[i] == sn[i + N]:
            return False
    return True

if __name__ == "__main__":
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        Path[Not(a)].append(b if b > 0 else -b + N)
        Path[Not(b)].append(a if a > 0 else -a + N)

    for i in range(1, 2 * N + 1):
        if scc_id[i] == 0:
            dfs(i)
    
    print(1 if Check() else 0)
