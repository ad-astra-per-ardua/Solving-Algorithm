import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

MAX_N = 30001
MAX_K = 3001
N, M, K = map(int, input().split())
C = [0] + list(map(int, input().split())) + [0] * (MAX_N - N - 1)
Parent = [i for i in range(MAX_N)]
Friends = [[] for _ in range(MAX_N)]
All_Candy = [0 for _ in range(MAX_N)]
DP = [[0]*MAX_K for _ in range(MAX_N)]
Answer = 0

def find(x):
    if Parent[x] == x:
        return x
    return find(Parent[x])

def union(x, y):
    px = find(x)
    py = find(y)
    if px <= py:
        Parent[py] = px
    else:
        Parent[px] = py

for _ in range(M):
    A, B = map(int, input().split())
    union(A, B)

Vec = []
for i in range(1, N+1):
    P = find(i)
    Friends[P].append(i)
    Vec.append(P)

Vec = sorted(list(set(Vec)))
for i in range(len(Vec)):
    rep = Vec[i]
    for j in range(len(Friends[rep])):
        All_Candy[i] += C[Friends[rep][j]]

for i in range(len(Vec)):
    cur = Vec[i]
    cnt = len(Friends[cur])
    candy = All_Candy[i]
    for j in range(K-1, -1, -1):
        if j - cnt >= 0:
            DP[i+1][j] = max(DP[i][j], DP[i][j-cnt] + candy)
        else:
            DP[i+1][j] = DP[i][j]
        Answer = max(Answer, DP[i+1][j])

print(Answer)
