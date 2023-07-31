import sys
input = sys.stdin.readline

par = []
ans = list()
n = int(input())
for _ in range(n):
    par.append(list(map(str, input().split())))
ans = list(map(str, input().split()))

for temp in ans:
    cor = False
    for idx in range(n):
        if len(par[idx]) != 0:
            if temp == par[idx][0]:
                par[idx].pop(0)
                cor = True
                break
    if not cor:
        break

left = 0
for line in par:
    left += len(line)
if cor and left == 0:
    print("Possible")
else:
    print("Impossible")