n = int(input())
v = []


def combination(n, r):
    var = 1
    for i in range(r):
        var *= n - i
    for i in range(r):
        var //= r - i
    return var


for r in range(1, 31):
    low, high = r << 1, n + 1
    while low + 1 < high:
        mid = low + high >> 1
        if combination(mid, r) <= n:
            low = mid
        else:
            high = mid
    if combination(low, r) == n:
        v.append((low, r))
        if r < low - r: 
            v.append((low, low - r))

v.sort(key=lambda x: (x[0], x[1]))

print(len(v))
for [a, b] in v:
    print(a,b)
