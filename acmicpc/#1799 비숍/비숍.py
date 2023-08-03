import sys
input = sys.stdin.readline
n = int(input())

chess = []
black = []
white = []
clr = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        clr[i][j] = (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)

for i in range(n):
    chess.append(list(map(int, input().split())))
    for j in range(n):
        if chess[i][j] == 1 and clr[i][j] == 1:
            black.append((i, j))
        elif chess[i][j] == 1 and clr[i][j] == 0:
            white.append((i, j))

b_cnt = 0
w_cnt = 0

used1 = [0]*(n*2-1)
used2 = [0]*(n*2-1)

def solve(bishop, idx, cnt):
    global b_cnt, w_cnt
    if idx == len(bishop):
        rx, ry = bishop[idx-1]
        if clr[rx][ry]:
            b_cnt = max(b_cnt, cnt)
        else:
            w_cnt = max(w_cnt, cnt)
        return

    x, y = bishop[idx]
    if used1[x+y] or used2[x-y+n-1]:
        solve(bishop, idx+1, cnt)
    else:
        used1[x+y] = 1
        used2[x-y+n-1] = 1
        solve(bishop, idx+1, cnt+1)
        used1[x+y] = 0
        used2[x-y+n-1] = 0
        solve(bishop, idx+1, cnt)

if len(black) > 0:
    solve(black, 0, 0)
if len(white) > 0:
    solve(white, 0, 0)
print(b_cnt + w_cnt)
