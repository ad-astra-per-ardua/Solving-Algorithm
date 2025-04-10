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

m_sieve = 200000
sieve = [0] * (m_sieve + 1)

for i in range(2, m_sieve + 1):
    if sieve[i] == 0:
        sieve[i] = i
        for j in range(i*2, m_sieve+1, i):
            if sieve[j] == 0:
                sieve[j] = i

def moebius(x):
    if x == 1:
        return 1
    last_p = -1
    cnt = 0
    while x > 1:
        p = sieve[x]
        if p == last_p:
            return 0
        x //= p
        if x % p == 0:
            return 0
        last_p = p
        cnt += 1
    return -1 if cnt % 2 else 1

def trial(x):
    sq = 0
    i = 1
    while i * i <= x:
        mu = moebius(i)
        if mu != 0:
            sq += mu * (x // (i*i))
        i += 1
    return x - sq

def main(n):
    low, high = 1, 4 * 10**10
    while low < high:
        mid = (low + high) // 2
        if trial(mid) >= n:
            high = mid
        else:
            low = mid + 1
    return low


if __name__ == "__main__":
    n = int(input())
    print(main(n))
