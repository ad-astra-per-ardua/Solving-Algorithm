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
# inter direction for graph traversal DFS,BFS Etc...
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# MOD = 1_000_000_007
# interrecursionlimit(10**6)
# input = lambda: stdin.readline().strip()

######### main code goes here #########


import sys
from collections import deque
from math import sqrt

input = sys.stdin.read

class Query:
    def __init__(self, s, e, x):
        self.s = s
        self.e = e
        self.x = x
    
    def __lt__(self, other):
        if self.s // sq != other.s // sq:
            return self.s < other.s
        return self.e < other.e

def plus(x, dir):
    global cnt, bucket, pos, arr
    now = 0
    dq = pos[arr[x]]
    if dq:
        now = dq[-1] - dq[0]
        cnt[now] -= 1
        bucket[now // sq] -= 1
    if dir == 0:
        dq.appendleft(x)
    else:
        dq.append(x)
    now = dq[-1] - dq[0]
    cnt[now] += 1
    bucket[now // sq] += 1

def minus(x, dir):
    global cnt, bucket, pos, arr
    dq = pos[arr[x]]
    now = dq[-1] - dq[0]
    cnt[now] -= 1
    bucket[now // sq] -= 1
    if dir == 0:
        dq.popleft()
    else:
        dq.pop()
    if dq:
        now = dq[-1] - dq[0]
        cnt[now] += 1
        bucket[now // sq] += 1

def query():
    global bucket, cnt
    for i in range(len(bucket) - 1, -1, -1):
        if bucket[i] > 0:
            for j in range(sq - 1, -1, -1):
                if cnt[i * sq + j] > 0:
                    return i * sq + j
    return 0

if __name__ == "__main__":
    data = input().split()
    idx = 0
    
    n = int(data[idx])
    k = int(data[idx + 1])
    idx += 2
    
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = int(data[idx])
        idx += 1
    
    q = int(data[idx])
    idx += 1
    
    queries = []
    for i in range(q):
        s = int(data[idx])
        e = int(data[idx + 1])
        queries.append(Query(s, e, i))
        idx += 2
    
    sq = int(sqrt(n)) + 1
    sz = (n // sq) + 10
    pos = [deque() for _ in range(101010)]
    cnt = [0] * (101010)
    bucket = [0] * sz
    ans = [0] * q
    
    queries.sort()
    
    s = queries[0].s
    e = queries[0].e
    x = queries[0].x
    
    for i in range(s, e + 1):
        plus(i, 1)
    ans[x] = query()
    
    for i in range(1, q):
        x = queries[i].x
        while queries[i].s < s:
            plus(s - 1, 0)
            s -= 1
        while e < queries[i].e:
            plus(e + 1, 1)
            e += 1
        while s < queries[i].s:
            minus(s, 0)
            s += 1
        while queries[i].e < e:
            minus(e, 1)
            e -= 1
        ans[x] = query()
    
    print("\n".join(map(str, ans)))

