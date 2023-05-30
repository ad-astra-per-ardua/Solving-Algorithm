import sys,math
input = sys.stdin.readline
rounds, kim, lim = map(int,input().split())
count = 0
while kim != lim:
    kim = math.ceil(kim / 2)
    lim = math.ceil(lim / 2)
    count += 1
    if kim == lim:
        break
print(count)