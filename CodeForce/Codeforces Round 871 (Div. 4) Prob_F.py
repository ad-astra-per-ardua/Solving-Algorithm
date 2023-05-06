def solve():
    n, m = [int(x) for x in input().split(' ')]
    t = [0] * (n + 1)
    for i in range(0, m):
        u, v = [int(x) for x in input().split(' ')]
        t[u] += 1
        t[v] += 1
    mp = {}
    for i in range(1, n + 1):
        if t[i] == 1:
            continue
        if mp.get(t[i], -1) == -1:
            mp[t[i]] = 0
        mp[t[i]] += 1
    a, b = 0, 0
    for x in mp:
        if mp[x] == 1:
            b = x
        else:
            a = x
    if b == 0:
        b = a
    print(f'{b} {a - 1}')
    pass


if __name__ == '__main__':
    _ = int(input())
    while _ > 0:
        solve()
        _ -= 1
