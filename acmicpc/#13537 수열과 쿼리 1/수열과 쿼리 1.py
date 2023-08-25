import sys
input = sys.stdin.readline

TN = 1 << 17
MN = 100000 + 10

N = 0
M = 0
A = [0] * MN
T = [0] * (2 * TN)
ans = [0] * MN
queries = []

class Query:
    def __init__(self, type_, idx, i, j, k):
        self.type = type_
        self.idx = idx
        self.i = i
        self.j = j
        self.k = k

def add(n, v):
    n += TN
    while n > 0:
        T[n] += v
        n //= 2

def get_sum(l, r):
    res = 0
    l += TN
    r += TN
    while l <= r:
        if l % 2 == 1:
            res += T[l]
            l += 1
        if r % 2 == 0:
            res += T[r]
            r -= 1
        l //= 2
        r //= 2

    return res

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    queries.append(Query(1, i, 0, 0, A[i]))

M = int(input())

for _ in range(M):
    i, j, k = map(int, input().split())
    queries.append(Query(2, _, i-1, j-1, k))

queries.sort(key=lambda q: (-q.k, -q.type))

for q in queries:
    if q.type == 1:
        add(q.idx, 1)
    if q.type == 2:
        ans[q.idx] = get_sum(q.i, q.j)

for m in range(M):
    print(ans[m])
