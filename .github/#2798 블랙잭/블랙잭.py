import sys, math
from sys import stdin, setrecursionlimit, stdout

def lcm(x, y):
    return x * y // math.gcd(x, y)
def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)
def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
def ceil(x):
    return int(x) if (x == int(x)) else int(x) + 1
def ceildiv(x, d):
    return x // d if (x % d == 0) else x // d + 1
def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
# setrecursionlimit(1_000_000)
dx = [1, 0, -1, 0, 1, -1, -1, 1]
dy = [0, 1, 0, -1, 1, 1, -1, -1]

input = lambda: stdstr().strip()

######### End of template #########
from bisect import bisect_right
n, m = map(int, input().split())
decks = list(map(int, input().split()))
decks.sort()
ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        p = decks[i] + decks[j]
        if p >= m:
            continue
        r = m - p
        idx = bisect_right(decks, r, j + 1) - 1
        if idx > j:
            t = p + decks[idx]
            if t > ans:
                ans = t
                if ans == m:
                    print(m)
                    sys.exit(0)

print(ans)
