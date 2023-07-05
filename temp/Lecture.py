import sys
input = sys.stdin.readline

t = int(input())
hgt = []
wid = []
tot = []
for i in range(6):
    direction, length = map(int, sys.stdin.readline().split())
    if direction == 1 or direction ==2:
        wid.append(length)
        tot.append(length)
    else:
        hgt.append(length)
        tot.append(length)

b = max(hgt) * max(wid)

mh = tot.index(max(hgt))
mw = tot.index(max(wid))

s1 = abs(tot[mh-1] - tot[(mh-5 if mh == 5 else mh +1)])

s2 = abs(tot[mw-1] - tot[(mw-5 if mw == 5 else mw +1)])
ans = (b - (s1 * s2)) * t
print(ans)