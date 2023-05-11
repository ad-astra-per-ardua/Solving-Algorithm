ans = 0
alist = []
for _ in range(10):
    a, b = map(int, input().split())
    ans -= a
    ans += b
    alist.append(ans)
alist.sort()
print(alist[9])