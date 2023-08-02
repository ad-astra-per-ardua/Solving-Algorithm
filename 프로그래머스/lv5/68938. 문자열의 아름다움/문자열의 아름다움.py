from collections import defaultdict
from itertools import groupby
def solution(s):
    l = defaultdict(lambda: defaultdict(int))
    for c, g in groupby(s):
        l[c][len(list(g))] += 1
    u = ((n := len(s)) - 1) * n * (n + 1) // 6
    for v in l.values():
        t = sum(lc * count for lc, count in v.items())
        b = sum(v.values())
        for i in range(1, max(v) + 1):
            u -= t * (t - 1) // 2
            t -= b
            b -= v[i]
    return u
