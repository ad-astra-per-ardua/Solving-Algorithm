import sys
from sys import stdin, setrecursionlimit
from math import gcd, lcm, perm, comb, sqrt
import heapq as hq
from types import GeneratorType
def ceil(x): return int(x) if(x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if(x % d == 0) else x//d+1

MOD = 1_000_000_007
# setrecursionlimit(10**6)
input = lambda: stdin.readline().strip()

######### main code goes here #########

MAXN = 2001
is_prime = [True] * (MAXN + 1)

def sieve_eratos():
    sqrtn = int(sqrt(MAXN))
    is_prime[0], is_prime[1] = False, False
    for i in range(2, sqrtn + 1):
        if is_prime[i]:
            for j in range(i * i, MAXN + 1, i):
                is_prime[j] = False

def dfs(a_idx):
    if a_idx == 0 or visited[a_idx]:
        return False
    visited[a_idx] = True

    for b_idx in adj[a_idx]:
        if b_match[b_idx] == -1 or dfs(b_match[b_idx]):
            a_match[a_idx] = b_idx
            b_match[b_idx] = a_idx
            return True
    return False

arr_size = int(input())
numbers = list(map(int, input().split()))
first_num = numbers[0]

a_set, b_set = [first_num], []

for temp in numbers[1:]:
    if first_num % 2:
        a_set.append(temp) if temp % 2 else b_set.append(temp)
    else:
        b_set.append(temp) if temp % 2 else a_set.append(temp)

if len(b_set) != len(a_set):
    print(-1)
    sys.exit(0)

sieve_eratos()

adj = [[] for _ in range(len(a_set))]
for i in range(len(a_set)):
    for j in range(len(b_set)):
        if is_prime[a_set[i] + b_set[j]]:
            adj[i].append(j)

answers = []
for i in range(len(adj[0])):
    pair_b_idx = adj[0][i]
    paired_size = 1

    a_match = [-1] * len(a_set)
    b_match = [-1] * len(b_set)

    a_match[0] = pair_b_idx
    b_match[pair_b_idx] = 0

    for j in range(1, len(a_set)):
        visited = [False] * len(a_set)
        if dfs(j):
            paired_size += 1

    if paired_size == len(b_set):
        answers.append(b_set[pair_b_idx])

if answers:
    answers.sort()
    print(' '.join(map(str, answers)))
else:
    print(-1)