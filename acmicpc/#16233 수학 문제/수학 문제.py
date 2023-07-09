import sys
input = sys.stdin.readline

def solve():
    f = [0]*100001
    for i in range(1, 100001):
        f[i] = f[i//10] + i%10

    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        ans = -1
        for x in range(n, n+90):
            if x < 100000:
                if x == n + f[x]:
                    ans = x
                    break
            else:
                if x == n + f[x//100000] + f[x%100000]:
                    ans = x
                    break
        results.append(str(ans))

    print(' '.join(results))

solve()
