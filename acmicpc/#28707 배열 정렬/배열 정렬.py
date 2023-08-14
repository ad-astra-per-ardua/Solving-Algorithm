import sys
import heapq as hq
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    mani = [list(map(int,input().split())) for _ in range(m)]
    for temp in mani:
        temp[0] -= 1
        temp[1] -=1
    fiv = set()
    queue = [(0,tuple(a))]
    while queue:
        d, v = hq.heappop(queue)
        if v in fiv:
            continue
        fiv.add(v)
        if all(v[i] <= v[i+1] for i in range(n-1)):
            print(d)
            return
        for a, b, c in mani:
            t = list(v)
            t[a] , t[b] = t[b], t[a]
            hq.heappush(queue, (d+c, tuple(t)))
    print(-1)

solve()