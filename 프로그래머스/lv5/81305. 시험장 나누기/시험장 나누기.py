import sys

sys.setrecursionlimit(10**6)

l = [0] * 10005
r = [0] * 10005
x = [0] * 10005
p = [-1] * 10005
root = 0
cnt = 0

def dfs(cur, lim):
    global cnt
    lv = 0
    if l[cur] != -1: lv = dfs(l[cur], lim)
    rv = 0
    if r[cur] != -1: rv = dfs(r[cur], lim)

    min_val = min(lv, rv)
    
    if x[cur] + lv + rv <= lim:
        return x[cur] + lv + rv
    if x[cur] + min_val <= lim:
        cnt += 1
        return x[cur] + min_val
    cnt += 2
    return x[cur]

def solve(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1
    return cnt

def solution(k, num, links):
    global root
    n = len(num)
    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1: p[l[i]] = i
        if r[i] != -1: p[r[i]] = i

    for i in range(n):
        if p[i] == -1:
            root = i
            break

    st = max(x)
    en = 10 ** 8
    while st < en:
        mid = (st + en) // 2
        if solve(mid) <= k:
            en = mid
        else:
            st = mid + 1
    return st
