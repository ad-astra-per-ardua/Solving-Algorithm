t = int(input())
for tt in range(t):
    n, q = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    pref = [0] * (n + 1)
    s = 0
    ans = ''
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
        s += a[i]
    for i in range(q):
        l, r, k = map(int, input().split(' '))
        cur = s - pref[r] + pref[l - 1] + k * (r - l + 1)
        cur %= 2
        if cur == 1:
            ans += "YES\n"
        else:
            ans += "NO\n"
    print(ans, end='')
